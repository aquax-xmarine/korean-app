#!/usr/bin/env python3
"""
Chinese Vocabulary Video Generator
Usage: python lesson4.py lesson4.mp3 lesson4.mp4

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

# ── Data ──────────────────────────────────────────────────────────────────────

VOCABULARY = [
    {"chinese": "在哪儿",  "pinyin": "zài nǎr",       "english": "where"},
    {"chinese": "一直走",  "pinyin": "yìzhí zǒu",     "english": "go straight ahead"},
    {"chinese": "停",      "pinyin": "tíng",           "english": "stop"},
    {"chinese": "左边",    "pinyin": "zuǒ biān",       "english": "left side"},
    {"chinese": "右边",    "pinyin": "yòu biān",       "english": "right side"},
    {"chinese": "左拐",    "pinyin": "zuǒ guǎi",       "english": "turn left"},
    {"chinese": "右拐",    "pinyin": "yòu guǎi",       "english": "turn right"},
    {"chinese": "前面",    "pinyin": "qián miàn",      "english": "front"},
    {"chinese": "后面",    "pinyin": "hòu miàn",       "english": "behind"},
    {"chinese": "您好",    "pinyin": "nín hǎo",        "english": "hello (formal)"},
    {"chinese": "多少钱",  "pinyin": "duō shǎo qián",  "english": "how much money"},
    {"chinese": "两块",    "pinyin": "liǎng kuài",     "english": "two dollars"},
    {"chinese": "谢谢",    "pinyin": "xiè xie",        "english": "thank you"},
    {"chinese": "六",      "pinyin": "liù",            "english": "six"},
    {"chinese": "再见",    "pinyin": "zài jiàn",       "english": "goodbye"},
]

TIMESTAMPS = [
    {"text":"在哪儿","pinyin":"zài nǎr","section":"teaching","start":20.11,"end":21.76},
    {"text":"在哪儿","pinyin":"zài nǎr","section":"teaching","start":29.17,"end":30.4},
    {"text":"在哪儿","pinyin":"zài nǎr","section":"teaching","start":33.58,"end":35.24},
    {"text":"一直走","pinyin":"yìzhí zǒu","section":"teaching","start":43.85,"end":45.29},
    {"text":"一直走","pinyin":"yìzhí zǒu","section":"teaching","start":53.54,"end":55.22},
    {"text":"一直走","pinyin":"yìzhí zǒu","section":"teaching","start":59.0,"end":60.44},
    {"text":"停","pinyin":"tíng","section":"teaching","start":68.82,"end":70.31},
    {"text":"停","pinyin":"tíng","section":"teaching","start":75.72,"end":76.8},
    {"text":"停","pinyin":"tíng","section":"teaching","start":80.2,"end":81.69},
    {"text":"一直走","pinyin":"yìzhí zǒu","section":"review","start":92.7,"end":94.14},
    {"text":"在哪儿","pinyin":"zài nǎr","section":"review","start":98.65,"end":100.3},
    {"text":"停","pinyin":"tíng","section":"review","start":103.81,"end":104.89},
    {"text":"左边","pinyin":"zuǒ biān","section":"teaching","start":112.47,"end":114.03},
    {"text":"左边","pinyin":"zuǒ biān","section":"teaching","start":119.18,"end":120.43},
    {"text":"右边","pinyin":"yòu biān","section":"teaching","start":125.03,"end":126.73},
    {"text":"右边","pinyin":"yòu biān","section":"teaching","start":132.1,"end":133.35},
    {"text":"左拐","pinyin":"zuǒ guǎi","section":"teaching","start":141.04,"end":142.72},
    {"text":"左拐","pinyin":"zuǒ guǎi","section":"teaching","start":147.88,"end":149.17},
    {"text":"左拐","pinyin":"zuǒ guǎi","section":"teaching","start":152.76,"end":154.44},
    {"text":"右拐","pinyin":"yòu guǎi","section":"teaching","start":160.8,"end":162.12},
    {"text":"右拐","pinyin":"yòu guǎi","section":"teaching","start":167.97,"end":169.72},
    {"text":"右拐","pinyin":"yòu guǎi","section":"teaching","start":173.27,"end":174.59},
    {"text":"左边","pinyin":"zuǒ biān","section":"review","start":185.76,"end":187.32},
    {"text":"右拐","pinyin":"yòu guǎi","section":"review","start":191.32,"end":192.64},
    {"text":"右边","pinyin":"yòu biān","section":"review","start":196.72,"end":198.43},
    {"text":"左拐","pinyin":"zuǒ guǎi","section":"review","start":202.68,"end":203.97},
    {"text":"一直走","pinyin":"yìzhí zǒu","section":"review","start":208.44,"end":210.12},
    {"text":"前面","pinyin":"qián miàn","section":"teaching","start":219.06,"end":220.36},
    {"text":"前面","pinyin":"qián miàn","section":"teaching","start":226.2,"end":227.84},
    {"text":"前面","pinyin":"qián miàn","section":"teaching","start":231.4,"end":232.7},
    {"text":"后面","pinyin":"hòu miàn","section":"teaching","start":238.89,"end":240.57},
    {"text":"后面","pinyin":"hòu miàn","section":"teaching","start":246.71,"end":247.96},
    {"text":"后面","pinyin":"hòu miàn","section":"teaching","start":251.48,"end":253.16},
    {"text":"后面","pinyin":"hòu miàn","section":"review","start":265.64,"end":266.89},
    {"text":"左拐","pinyin":"zuǒ guǎi","section":"review","start":271.14,"end":272.82},
    {"text":"前面","pinyin":"qián miàn","section":"review","start":276.97,"end":278.27},
    {"text":"在哪儿","pinyin":"zài nǎr","section":"review","start":282.49,"end":284.15},
    {"text":"右拐","pinyin":"yòu guǎi","section":"review","start":288.16,"end":289.48},
    {"text":"您好","pinyin":"nín hǎo","section":"review","start":306.64,"end":308.27},
    {"text":"右拐","pinyin":"yòu guǎi","section":"review","start":313.26,"end":314.58},
    {"text":"多少钱","pinyin":"duō shǎo qián","section":"review","start":320.29,"end":322.02},
    {"text":"两块","pinyin":"liǎng kuài","section":"review","start":327.2,"end":328.5},
    {"text":"一直走","pinyin":"yìzhí zǒu","section":"review","start":333.85,"end":335.53},
    {"text":"谢谢","pinyin":"xiè xie","section":"review","start":340.0,"end":341.27},
    {"text":"六","pinyin":"liù","section":"review","start":345.57,"end":347.2},
    {"text":"停","pinyin":"tíng","section":"review","start":351.0,"end":352.08},
    {"text":"再见","pinyin":"zài jiàn","section":"review","start":356.9,"end":358.53},
]

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
fonts_dir  = os.path.join(script_dir, "fonts")

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

def get_active_word(t):
    """Highlight persists from when a word is spoken until the next word starts."""
    last_idx = None
    for i, ts in enumerate(TIMESTAMPS):
        if ts["start"] <= t:
            last_idx = i
        else:
            break
    if last_idx is None:
        return None, None
    last   = TIMESTAMPS[last_idx]
    nxt    = TIMESTAMPS[last_idx + 1] if last_idx + 1 < len(TIMESTAMPS) else None
    end    = nxt["start"] if nxt else float("inf")
    if t < end:
        return last["text"], last["section"]
    return None, None

def is_review_section(t):
    _, section = get_active_word(t)
    if section:
        return section == "review"
    nxt = next((ts for ts in TIMESTAMPS if ts["start"] > t), None)
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
CARD_H = 210   # taller to fit bigger text
GAP_X  = 20
GAP_Y  = 18
GRID_W = COLS * CARD_W + (COLS - 1) * GAP_X
GRID_H = 3 * CARD_H + 2 * GAP_Y
GRID_X = (W - GRID_W) // 2
GRID_Y = 100 + (H - 100 - 80 - GRID_H) // 2

def draw_header(draw, t, section_label):
    draw.rectangle([0, 0, W, 90], fill=(16, 18, 24))
    draw.line([0, 90, W, 90], fill=BORDER, width=2)
    draw.text((64, 28), "CHINESE  ·  DIRECTIONS & NAVIGATION",
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
    fe = font(FONT_SANS_B, 24)
    ew, _ = text_size(draw, english, fe)
    draw.text((x + (CARD_W - ew) // 2, y + 150), english, font=fe, fill=en_col)

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

    c, m, cs = (60, 55, 30), 40, 40
    for a, b in [
        ([m, m+100, m+cs, m+100],       [m, m+100, m, m+100+cs]),
        ([W-m-cs, m+100, W-m, m+100],   [W-m, m+100, W-m, m+100+cs]),
        ([m, H-m-72, m+cs, H-m-72],     [m, H-m-72-cs, m, H-m-72]),
        ([W-m-cs, H-m-72, W-m, H-m-72], [W-m, H-m-72-cs, W-m, H-m-72]),
    ]:
        draw.line(a, fill=c, width=2)
        draw.line(b, fill=c, width=2)

    fr = font(FONT_SANS_B, 110)
    title = "REVIEW TIME"
    tw, _ = text_size(draw, title, fr)
    draw.text(((W - tw) // 2, 140), title, font=fr, fill=ACCENT)

    sub = "LISTEN  ·  RECALL  ·  RESPOND"
    sw, _ = text_size(draw, sub, font(FONT_SANS, 22))
    draw.text(((W - sw) // 2, 290), sub, font=font(FONT_SANS, 22), fill=TEXT_SEC)
    draw.line([W//2 - 120, 340, W//2 + 120, 340], fill=(60, 55, 30), width=2)

    if active_word:
        pinyin_map = {v["chinese"]: v["pinyin"] for v in VOCABULARY}
        ts_current = get_current_ts(t)

        # fade in at word start, stay fully visible while persisting
        if ts_current and ts_current["text"] == active_word:
            fade = min((t - ts_current["start"]) / 0.15, 1.0)
        else:
            fade = 1.0

        fc = font(FONT_CHINESE, 160)
        cw, _ = text_size(draw, active_word, fc)
        draw.text(((W - cw) // 2, 370), active_word, font=fc,
                  fill=lerp_color(BG, ACCENT, fade))

        py = pinyin_map.get(active_word, "")
        if py:
            fp = font(FONT_SANS, 42)   # 42px on review screen
            pw, _ = text_size(draw, py, fp)
            draw.text(((W - pw) // 2, 575), py, font=fp,
                      fill=lerp_color(BG, (160, 135, 70), fade))

# ── Frame renderer ────────────────────────────────────────────────────────────

_section_transition = [0.0]
TRANSITION_SPEED = 0.08

def render_frame(t):
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    active_word, active_section = get_active_word(t)
    review = (active_section == "review") if active_section else is_review_section(t)

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
    print(f"Reading audio: {audio_path}")
    duration     = get_audio_duration(audio_path)
    total_frames = int(duration * FPS)
    print(f"Duration: {duration:.1f}s  |  Frames: {total_frames}  |  Resolution: {W}x{H}")
    print(f"Output: {output_path}\n")

    frames_dir = os.path.join(os.path.dirname(os.path.abspath(output_path)), "frames_tmp")
    os.makedirs(frames_dir, exist_ok=True)

    print("Step 1/2: Rendering frames...")
    for i in range(total_frames):
        t = i / FPS
        Image.fromarray(render_frame(t)).save(
            os.path.join(frames_dir, f"frame_{i:05d}.png"))
        if i % FPS == 0 or i == total_frames - 1:
            pct     = (i + 1) / total_frames * 100
            elapsed = int(t)
            total   = int(duration)
            bar     = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
            print(f"\r  [{bar}] {pct:5.1f}%  {elapsed//60}:{elapsed%60:02d} / {total//60}:{total%60:02d}",
                  end="", flush=True)

    print("\n\nStep 2/2: Encoding with ffmpeg...")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", os.path.join(frames_dir, "frame_%05d.png"),
        "-i", audio_path,
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "16",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        output_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    print("Cleaning up temp frames...")
    shutil.rmtree(frames_dir)

    if result.returncode != 0:
        print("\nFFmpeg error:")
        print(result.stderr)
        sys.exit(1)

    print(f"\n✓ Done! Output: {output_path}  ({os.path.getsize(output_path)/1024/1024:.1f} MB)")

# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lesson4.py <audio.mp3> [output.mp4]")
        sys.exit(1)

    audio_in  = sys.argv[1]
    video_out = sys.argv[2] if len(sys.argv) > 2 else "output.mp4"

    if not os.path.exists(audio_in):
        print(f"Error: audio file not found: {audio_in}")
        sys.exit(1)

    generate_video(audio_in, video_out)