#!/usr/bin/env python3
"""
Chinese Vocabulary Video Generator
Usage: python lesson3.py lesson3.mp3 lesson3.mp4

Fonts required in a 'fonts' folder next to this script:
  NotoSerifSC-Bold.otf   <- https://fonts.google.com/noto/specimen/Noto+Serif+SC
  NotoSans-Regular.ttf   <- https://fonts.google.com/noto/specimen/Noto+Sans
  NotoSans-Bold.ttf      <- same zip as above
"""

import sys
import os
import subprocess
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import json
import threading



sys.path.append(
    r"C:\Users\NIKISHA\Documents\korean-app\frontend\text_to_speech\chinese"
)

from chinese_vocabulary import VOCABULARY as ALL_VOCABULARY

json_path = r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson3.json"

with open(json_path, "r", encoding="utf-8") as f:
    lesson_data = json.load(f)

# Only keep chinese words for vocabulary and timestamps
teaching_words = {ts["text"] for ts in lesson_data["timestamps"] if ts.get("is_chinese") and ts.get("section") == "teaching"}
VOCABULARY = [v for v in lesson_data["vocabulary"] if v["chinese"] in teaching_words]
TIMESTAMPS = [ts for ts in lesson_data["timestamps"] if ts.get("is_chinese")]

ALL_TIMESTAMPS = lesson_data["timestamps"]
# Add this near the top after loading lesson_data

CHAR_PINYIN = {}
for chars, info in ALL_VOCABULARY.items():
    pinyins = info["pinyin"].split()
    if len(chars) == len(pinyins):
        for ch, py in zip(chars, pinyins):
            CHAR_PINYIN[ch] = py

def get_pinyin(word):
    if word in ALL_VOCABULARY:
        return ALL_VOCABULARY[word]["pinyin"]
    parts = [CHAR_PINYIN.get(ch, "?") for ch in word]
    return " ".join(parts) if "?" not in parts else ""


# ── Config ────────────────────────────────────────────────────────────────────

W, H = 1920, 1080
FPS  = 24

BG         = (13, 15, 20)
SURFACE    = (22, 25, 32)
BORDER     = (40, 44, 56)
TEXT_PRI   = (240, 236, 228)
TEXT_SEC   = (110, 110, 120)
TEXT_DIM   = (70, 70, 78)
ACCENT     = (232, 200, 122)
ACCENT_DIM = (55, 48, 22)
ACCENT_MID = (160, 130, 60)

# ── Fonts ─────────────────────────────────────────────────────────────────────

script_dir = os.path.dirname(os.path.abspath(__file__))
fonts_dir  = fonts_dir  = r"C:\Users\NIKISHA\Documents\korean-app\frontend\text_to_video\chinese\fonts"

FONT_CHINESE = os.path.join(fonts_dir, "NotoSerifSC-Bold.otf")
FONT_SANS    = os.path.join(fonts_dir, "NotoSans-Regular.ttf")
FONT_SANS_B  = os.path.join(fonts_dir, "NotoSans-Bold.ttf")

for f_path in [FONT_CHINESE, FONT_SANS, FONT_SANS_B]:
    if not os.path.exists(f_path):
        print(f"\n ERROR: Missing font: {f_path}")
        print("  Place NotoSerifSC-Bold.ttf, NotoSans-Regular.ttf, NotoSans-Bold.ttf")
        print("  in a 'fonts' folder next to this script.")
        sys.exit(1)

_font_cache = {}
def font(path, size):
    key = (path, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]

# ── Helpers ───────────────────────────────────────────────────────────────────

def get_current_ts(t):
    for ts in TIMESTAMPS:
        if ts["start"] <= t < ts["end"]:
            return ts
    return None

def get_current_section(t):
    """Get the section of the most recent timestamp of any type."""
    last = None
    for ts in ALL_TIMESTAMPS:
        if ts["start"] <= t:
            last = ts
        else:
            break
    return last["section"] if last else "teaching"

def get_active_word(t):
    last_idx = None
    for i, ts in enumerate(TIMESTAMPS):
        if ts["start"] <= t:
            last_idx = i
        else:
            break

    current_section = get_current_section(t)  # ← use ALL_TIMESTAMPS

    if last_idx is None:
        return None, current_section

    last = TIMESTAMPS[last_idx]

    if current_section == "review":
        # Only show the word while it's actually being spoken
        if last["start"] <= t < last["end"] and last["section"] == "review":
            return last["text"], "review"
        else:
            return None, "review"  # narrator is speaking, still in review
    else:
        nxt = TIMESTAMPS[last_idx + 1] if last_idx + 1 < len(TIMESTAMPS) else None
        end = nxt["start"] if nxt else float("inf")
        if t < end:
            return last["text"], "teaching"
        return None, "teaching"

def is_review_section(t):
    # Find the most recent event of ANY type (narrator, chinese, pause)
    last = None
    for ts in ALL_TIMESTAMPS:
        if ts["start"] <= t:
            last = ts
        else:
            break
    if last:
        return last["section"] == "review"
    # Before anything starts, check what's coming next
    nxt = next((ts for ts in ALL_TIMESTAMPS if ts["start"] > t), None)
    if nxt and nxt["section"] == "review":
        return True
    return False

def lerp_color(c1, c2, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def ease_inout(t):
    return t * t * (3 - 2 * t)

def text_size(draw, text, fnt):
    bb = draw.textbbox((0, 0), text, font=fnt)
    return bb[2] - bb[0], bb[3] - bb[1]

def rounded_rect(draw, x, y, w, h, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=outline, width=width)

# ── Layout ────────────────────────────────────────────────────────────────────

COLS   = 5
CARD_W = 340
CARD_H = 230
GAP_X  = 20
GAP_Y  = 18
GRID_W = COLS * CARD_W + (COLS - 1) * GAP_X
GRID_H = 2 * CARD_H + 1 * GAP_Y        # 10 cards = 2 rows of 5
GRID_X = (W - GRID_W) // 2             # horizontal centre
GRID_Y = 90 + (H - 90 - 72 - GRID_H) // 2  # vertical centre between header & footer

def draw_header(draw, t, section_label):
    draw.rectangle([0, 0, W, 90], fill=(16, 18, 24))
    draw.line([0, 90, W, 90], fill=BORDER, width=2)
    draw.text((64, 28), "CHINESE  ·  ADVANCED NUMBERS",
              font=font(FONT_SANS_B, 22), fill=ACCENT)
    badge = f"SECTION: {section_label.upper()}"
    fb = font(FONT_SANS, 18)
    bw, _ = text_size(draw, badge, fb)
    draw.text((W - 64 - bw, 34), badge, font=fb, fill=TEXT_SEC)
    dur = max(ts["end"] for ts in TIMESTAMPS)
    pct = min(t / dur, 1.0)
    draw.rectangle([0, 88, W, 92], fill=(30, 32, 40))
    draw.rectangle([0, 88, int(W * pct), 92], fill=ACCENT)

def draw_footer(draw, t):
    draw.rectangle([0, H - 72, W, H], fill=(16, 18, 24))
    draw.line([0, H - 72, W, H - 72], fill=BORDER, width=2)
    draw.text((64, H - 50), f"{int(t)//60}:{int(t)%60:02d}",
              font=font(FONT_SANS, 20), fill=TEXT_SEC)
    hint = "LISTEN  ·  REPEAT  ·  REMEMBER"
    hw, _ = text_size(draw, hint, font(FONT_SANS, 16))
    draw.text((W - 64 - hw, H - 46), hint, font=font(FONT_SANS, 16), fill=(55, 57, 66))

def draw_vocab_card(draw, x, y, vocab, active):
    chinese = vocab["chinese"]
    pinyin  = vocab["pinyin"]
    english = vocab["english"].upper()

    if active:
        bg, border, ch_col, py_col, en_col = ACCENT_DIM, ACCENT, ACCENT, ACCENT_MID, (130, 105, 40)
    else:
        bg, border, ch_col, py_col, en_col = SURFACE, BORDER, TEXT_PRI, TEXT_SEC, TEXT_DIM

    rounded_rect(draw, x, y, CARD_W, CARD_H, 14,
                 fill=bg, outline=border, width=2 if active else 1)

    if active:
        draw.ellipse([x + CARD_W - 20, y + 14, x + CARD_W - 10, y + 24], fill=ACCENT)

    # Chinese — 52px
    fc = font(FONT_CHINESE, 52)
    cw, _ = text_size(draw, chinese, fc)
    draw.text((x + (CARD_W - cw) // 2, y + 14), chinese, font=fc, fill=ch_col)

    # Pinyin — 28px (up from 20px)
    fp = font(FONT_SANS, 28)
    pw, _ = text_size(draw, pinyin, fp)
    draw.text((x + (CARD_W - pw) // 2, y + 98), pinyin, font=fp, fill=py_col)

    # English — 24px bold (up from 17px)
    # English — wrap long text to 2 lines
    fe = font(FONT_SANS_B, 18)
    max_width = CARD_W - 24
    words = english.split()
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if text_size(draw, test, fe)[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    lines = lines[:3]  # max 3 lines
    line_h = 22
    start_y = y + 148
    for li, line in enumerate(lines):
        lw, _ = text_size(draw, line, fe)
        draw.text((x + (CARD_W - lw) // 2, start_y + li * line_h), line, font=fe, fill=en_col)

def draw_grid(draw, active_word):
    for i, vocab in enumerate(VOCABULARY):
        row = i // COLS
        col = i % COLS
        x = GRID_X + col * (CARD_W + GAP_X)
        y = GRID_Y + row * (CARD_H + GAP_Y)
        draw_vocab_card(draw, x, y, vocab,
                        vocab["chinese"] == active_word if active_word else False)

def draw_review(draw, active_word, t):
    draw.rectangle([0, 94, W, H - 72], fill=BG)

    # corner brackets
    c, m, cs = (60, 55, 30), 40, 40
    for a, b in [
        ([m, m+100, m+cs, m+100],       [m, m+100, m, m+100+cs]),
        ([W-m-cs, m+100, W-m, m+100],   [W-m, m+100, W-m, m+100+cs]),
        ([m, H-m-72, m+cs, H-m-72],     [m, H-m-72-cs, m, H-m-72]),
        ([W-m-cs, H-m-72, W-m, H-m-72], [W-m, H-m-72-cs, W-m, H-m-72]),
    ]:
        draw.line(a, fill=c, width=2)
        draw.line(b, fill=c, width=2)

    # content area midpoint
    content_top = 90
    content_bot = H - 72
    mid = (content_top + content_bot) // 2

    # measure all text blocks first
    fr   = font(FONT_SANS_B, 110)
    fsub = font(FONT_SANS, 22)
    fc   = font(FONT_CHINESE, 160)
    fp   = font(FONT_SANS, 42)

    title_h = draw.textbbox((0, 0), "REVIEW TIME", font=fr)[3]
    sub_h   = draw.textbbox((0, 0), "LISTEN  ·  RECALL  ·  RESPOND", font=fsub)[3]
    gap1    = 20   # title → sub
    gap2    = 20   # sub → divider
    divider_h = 2
    gap3    = 40   # divider → chinese char
    gap4    = 16   # char → pinyin


   # Fixed position for review header
    title_y = 180
    y = title_y

    # draw title
    tw, _ = text_size(draw, "REVIEW TIME", fr)
    draw.text(((W - tw) // 2, y), "REVIEW TIME", font=fr, fill=ACCENT)
    y += title_h + gap1

    # draw subtitle
    sub = "LISTEN  ·  RECALL  ·  RESPOND"
    sw, _ = text_size(draw, sub, fsub)
    draw.text(((W - sw) // 2, y), sub, font=fsub, fill=TEXT_SEC)
    y += sub_h + gap2

    # divider
    draw.line([W//2 - 120, y, W//2 + 120, y], fill=(60, 55, 30), width=2)
    divider_y = y
    word_y = divider_y + 80
    pinyin_y = word_y + 240

    if active_word:
        ts_current = get_current_ts(t)

        fade = (
            min((t - ts_current["start"]) / 0.15, 1.0)
            if ts_current and ts_current["text"] == active_word
            else 1.0
        )

        cw, _ = text_size(draw, active_word, fc)

        draw.text(
            ((W - cw) // 2, word_y),
            active_word,
            font=fc,
            fill=lerp_color(BG, ACCENT, fade)
        )

        py = get_pinyin(active_word)

        if py:
            pw, _ = text_size(draw, py, fp)

            draw.text(
                ((W - pw) // 2, pinyin_y),
                py,
                font=fp,
                fill=lerp_color(BG, (160, 135, 70), fade)
            )

# ── Frame renderer ────────────────────────────────────────────────────────────

_section_transition = [0.0]
TRANSITION_SPEED = 0.08

def render_frame(t):
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    active_word, active_section = get_active_word(t)
    review = (active_section == "review")

    target = 1.0 if review else 0.0
    cur    = _section_transition[0]
    diff   = target - cur
    cur   += TRANSITION_SPEED if diff > 0 else -TRANSITION_SPEED
    if abs(diff) < TRANSITION_SPEED:
        cur = target
    _section_transition[0] = cur

    grid_vis = 1.0 - ease_inout(cur)

    if grid_vis > 0.02:
        draw_grid(draw, active_word if not review else None)
        if grid_vis < 1.0:
            overlay = Image.new("RGB", (W, H), BG)
            img  = Image.blend(img, overlay, 1.0 - grid_vis)
            draw = ImageDraw.Draw(img)

    if cur > 0.02:
        rev_img  = Image.new("RGB", (W, H), BG)
        rev_draw = ImageDraw.Draw(rev_img)
        draw_review(rev_draw, active_word if review else None, t)
        blended = Image.blend(Image.new("RGB", (W, H), BG), rev_img, ease_inout(cur))
        img  = Image.blend(img, blended, ease_inout(cur))
        draw = ImageDraw.Draw(img)

    draw_header(draw, t, "review" if review else "teaching")
    draw_footer(draw, t)

    return np.array(img)

# ── Video generation ──────────────────────────────────────────────────────────

def get_audio_duration(audio_path):
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", audio_path],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())


def generate_video(audio_path, output_path):
    duration     = get_audio_duration(audio_path)
    total_frames = int(duration * FPS)

    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{W}x{H}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "pipe:0",
        "-i", audio_path,
        "-c:v", "h264_nvenc",
        "-preset", "p4",
        "-cq", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        output_path
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    # Read stderr in background to prevent deadlock
    stderr_lines = []
    def read_stderr():
        for line in proc.stderr:
            stderr_lines.append(line.decode(errors="replace"))
    t_err = threading.Thread(target=read_stderr, daemon=True)
    t_err.start()

    for i in range(total_frames):
        t = i / FPS
        frame = render_frame(t)
        try:
            proc.stdin.write(frame.tobytes())
        except BrokenPipeError:
            t_err.join()
            print("\nffmpeg pipe broke:")
            print("".join(stderr_lines))
            sys.exit(1)
        if i % FPS == 0:
            pct = (i + 1) / total_frames * 100
            print(f"\r  {pct:.1f}%  {int(t)//60}:{int(t)%60:02d}", end="", flush=True)

    proc.stdin.close()
    proc.wait()
    t_err.join()

    if proc.returncode != 0:
        print("\nffmpeg error:")
        print("".join(stderr_lines))
        sys.exit(1)
    else:
        size_mb = os.path.getsize(output_path) / 1024 / 1024
        print(f"\n✓ Done! {output_path} ({size_mb:.1f} MB)")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lesson3.py <audio.mp3> [output.mp4]")
        sys.exit(1)

    audio_in  = sys.argv[1]
    video_out = sys.argv[2] if len(sys.argv) > 2 else "output.mp4"

    if not os.path.exists(audio_in):
        print(f"Error: audio file not found: {audio_in}")
        sys.exit(1)

    generate_video(audio_in, video_out)