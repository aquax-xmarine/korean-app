import asyncio
import edge_tts
from pydub import AudioSegment
import json
import re
import sys
sys.path.append(r"C:\Users\NIKISHA\Documents\korean-app\frontend\text_to_speech\chinese")
from chinese_vocabulary import VOCABULARY

# =========================
# VOICE CONFIGURATION
# =========================

NARRATOR_VOICE = "en-US-AvaMultilingualNeural"
CHINESE_MALE = "zh-CN-YunxiNeural"
CHINESE_FEMALE = "zh-CN-XiaoxiaoNeural"

# =========================
# LESSON SCRIPT
# =========================

script = [
    # =========================================================
    # INTRODUCTION & THE RULE OF TWO
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Welcome to Level 1, Topic 3 of your Chinese Audio Coach. Today we handle advanced numbers, massive counting scales, and currency. First, we must master a critical rule. When counting physical items or specifying 'two' of something, Chinese switches from èr to a completely different word. Listen closely."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "两。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Notice the dipping and rising tone: Liǎng. Use this for two people, two hours, or two dollars. Never use èr for quantities. Listen again."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "两。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Two of something."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "两。"
    },
    {
        "section": "teaching",
        "pause": 2000 
    },

    # =========================================================
    # MODULE 1: THOUSANDS & TEN-THOUSANDS (THE LINGUISTIC SHIFT)
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Now let's scale up. To say Thousand, we use a sharp dropping tone. Thousand."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "千。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Pronounced high and flat: Qiān. Let's make it One Thousand."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "一千。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. One Thousand."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "一千。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Unlike English which groups numbers by thousands, Chinese groups large numbers by four digits—meaning ten-thousand gets its own unique base word. Ten-Thousand."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "万。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "A sharp, definitive falling tone: Wàn. Let's say One Ten-Thousand."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "一万。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Ten Thousand."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "一万。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK A: SCALE FOUNDATIONS
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Let's pause and anchor these base scales. Speak your answers instantly. One Thousand."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "一千。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Ten Thousand."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "一万。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "How do you say 'two' when counting physical objects?"
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "两。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "One Hundred from our previous lesson."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "一百。"
    },

    # =========================================================
    # MODULE 2: MILLIONS & CASH TERMINOLOGY
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Moving to Module 2. Because of the four-digit grouping system, One Million is expressed literally as 'One Hundred Ten-Thousands'. One Million."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "一百万。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the compounding blocks: Yì bǎi wàn. One Million."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "一百万。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. One Million."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "一百万。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Now let's talk money. The formal name for Chinese currency is the Renminbi, but in daily life, people use the word for 'piece' or 'bucket' to count money. Dollar."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "块。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "A strong, falling tone: Kuài. Let's combine it with our new quantity rule to say Two Dollars."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "两块。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Notice it uses liǎng, never èr. Two Dollars."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "两块。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Two Dollars."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "两块。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "To ask 'How much money is it?' when shopping, a native speaker says."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "多少钱？"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the cadence: Duōshǎo qián? How much money? Listen again."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "多少钱？"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat this essential shopping phrase. How much money?"
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "多少钱？"
    },
    {
        "section": "teaching",
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK B: ADVANCED COMBINATIONS
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Let's drill these financial patterns. Give me the Chinese translation during the silence. Two Dollars."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "两块。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "How much money?"
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "多少钱？"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "One Million."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "一百万。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Ten Dollars."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "十块。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 1: ADVANCED NUMBERS)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "You have unlocked the full core numeric scaling grid. Let's enter the deep-retention challenge loop. Translate the advanced metrics instantly. One Thousand."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "一千。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "How much money?"
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "多少钱？"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Two of something."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "两。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Ten Thousand."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "一万。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Two Dollars."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "两块。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "One Million."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "一百万。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 2: DEEP LESSONS 1-3 CROSS BRIDGE)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Phenomenal. Now we execute an ultimate triple-topic integration drill. This combines greetings, primary numbers, and transaction scales. Stay highly responsive. Say: Hello."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "你好。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Eight Dollars."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "八块。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Thank you."
    },
    {
        "section": "review",
        "pause": 1500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Five Thousand."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "五千。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Goodbye."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "再见。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: How much money?"
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "多少钱？"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: I'm sorry."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "对不起。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Two (the digit used for counting math, not objects)."
    },
    {
        "section": "review",
        "pause": 1500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "二。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Two Dollars (using the quantity format)."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "两块。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Correct."
    },
    {
        "section": "review",
        "pause": 1500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "对。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Unbelievable fluency. You have locked down the foundational grammar, core vocabulary, and transactional metrics of basic Mandarin Chinese. Class dismissed."
    }
]



# =========================
# VOICE SELECTOR
# =========================

def get_voice(voice_type):
    if voice_type == "narrator":
        return NARRATOR_VOICE
    elif voice_type == "male":
        return CHINESE_MALE
    elif voice_type == "female":
        return CHINESE_FEMALE
    return NARRATOR_VOICE

# =========================
# GENERATE SINGLE AUDIO
# =========================


async def generate_tts(text, voice, output_file, retries=3):
    for attempt in range(retries):
        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice=voice
            )
            await communicate.save(output_file)
            return
        except Exception as e:
            print(f"  Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(2)
            else:
                raise


# =========================
# BUILD FULL LESSON
# =========================

async def build_lesson():

    combined = AudioSegment.empty()

    vocabulary = {}

    timestamps = []
    current_ms = 0

    for idx, item in enumerate(script):

        # Handle pauses
        if "pause" in item:
            timestamps.append({
                "text": "[pause]",
                "pinyin": "",
                "english": "",
                "section": item["section"],
                "voice": "pause",
                "is_chinese": False,
                "start": round(current_ms / 1000, 2),
                "end": round((current_ms + item["pause"]) / 1000, 2)
            })
            silence = AudioSegment.silent(duration=item["pause"])
            combined += silence
            current_ms += item["pause"]
            continue

        voice = get_voice(item["voice"])
        text = item["text"]

        if re.search(r'[\u4e00-\u9fff]', text):

            clean_text = (
                text.replace("。", "")
                    .replace("？", "")
                    .replace("！", "")
            )

            if clean_text in VOCABULARY:
                vocabulary[clean_text] = {
                    "chinese": clean_text,
                    "pinyin": VOCABULARY[clean_text]["pinyin"],
                    "english": VOCABULARY[clean_text]["english"]
                }

        filename = f"temp_{idx}.mp3"

        print(f"Generating: {text[:40]}")

        await generate_tts(text, voice, filename)

        segment = AudioSegment.from_mp3(filename)

        duration = len(segment)

        # Save timestamps for everything
        is_chinese = bool(re.search(r'[\u4e00-\u9fff]', text))
        clean_text = text.replace("。", "").replace("？", "").replace("！", "") if is_chinese else text

        timestamps.append({
            "text": clean_text,
            "pinyin": VOCABULARY.get(clean_text, {}).get("pinyin", "") if is_chinese else "",
            "english": VOCABULARY.get(clean_text, {}).get("english", "") if is_chinese else "",
            "section": item["section"],
            "voice": item["voice"],
            "is_chinese": is_chinese,
            "start": round(current_ms / 1000, 2),
            "end": round((current_ms + duration) / 1000, 2)
        })

        combined += segment

        current_ms += duration

        # Natural pause
        combined += AudioSegment.silent(duration=500)

        current_ms += 500

    # Export MP3
    mp3_path = r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson3.mp3"

    combined.export(mp3_path, format="mp3")

    # Export timestamps JSON
    json_path = r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson3.json"

    lesson_data = {
        "vocabulary": list(vocabulary.values()),
        "timestamps": timestamps
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            lesson_data,
            f,
            ensure_ascii=False,
            indent=2
        )

    print("Finished!")
    print(f"Audio: {mp3_path}")
    print(f"Timestamps: {json_path}")


# =========================
# RUN
# =========================

asyncio.run(build_lesson())
