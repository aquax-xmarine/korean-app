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
    # INTRODUCTION
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Welcome to Level 1, Topic 2 of your Chinese Audio Coach. Today we are mastering numbers. Chinese numbers follow a beautifully logical pattern, but you must nail the tones to be understood. Speak out loud during every pause. Let's start with zero."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "零。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Notice the rising tone, like asking a question: Ling. Zero."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "零。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Zero."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "零。"
    },
    {
        "section": "teaching",
        "pause": 2000 
    },

    # =========================================================
    # MODULE 1: NUMBERS 1 TO 3
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Let's build the first sequence. The number One is a flat, high pitch. One."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "一。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Keep your pitch high and steady: Yi. One."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "一。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "The number Two is a sharp, dropping tone. Two."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "二。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Drop your pitch with confidence: Èr. Two."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "二。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "The number Three returns to a high, flat pitch. Three."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "三。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the steady energy: San. Three."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "三。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Now, repeat the sequence one through three after the speaker. One, Two, Three."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "一，二，三。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK A: 0 TO 3 REPETITION
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Let's check your foundation. Say the Chinese numbers instantly during the pauses. Zero."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "零。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Three."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "三。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "One."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "一。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Two."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "二。"
    },

    # =========================================================
    # MODULE 2: NUMBERS 4 TO 6
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Moving to Module 2. The number Four is a sharp downward tone, hitting a crisp 's' sound. Four."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "四。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Make it short and punchy: Si. Four."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "四。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "The number Five scoop downwards and climbs back up. Five."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "五。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Let your pitch dip low: Wu. Five."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "五。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "The number Six drops sharply. Six."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "六。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Pronounced like 'liou' with a falling pitch: Liu. Six."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "六。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Now challenge yourself. Repeat four, five, six."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "四，五，六。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK B: CUMULATIVE 0 TO 6
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Let's combine both blocks. Keep your focus sharp. Say: Four."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "四。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Two."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "二。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Five."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "五。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Three."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "三。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Six."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "六。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "One."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "一。"
    },

    # =========================================================
    # MODULE 3: NUMBERS 7 TO 10
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Module 3 finishes the base sequence. The number Seven is high and flat. Seven."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "七。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Keep it high and thin: Qi. Seven."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "七。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "The number Eight is also high and flat. In Chinese culture, this is the luckiest number. Eight."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "八。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "High and level pitch: Ba. Eight."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "八。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "The number Nine dips deeply before rising. Nine."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "九。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Scoop your pitch low: Jiu. Nine."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "九。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "The number Ten climbs steadily upward. Ten."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "十。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Rise from low to high, curling your tongue slightly: Shi. Ten."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "十。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Let's lock in seven through ten. Repeat out loud."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "七，八，九，十。"
    },
    {
        "section": "teaching",
        "pause": 3000
    },

    # =========================================================
    # RECALL BLOCK C: CUMULATIVE 0 TO 10
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Let's consolidate the entire structure from zero to ten. Stay loose and match the tones. Say: Ten."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "十。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Seven."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "七。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Eight."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "八。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Nine."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "九。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Five."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "五。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Zero."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "零。"
    },

    # =========================================================
    # MODULE 4: HUNDRED & LESSON 1 RECALL BRIDGING
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "In Module 4, let's look at how to expand your scope. To say 'One Hundred', we use the word for one, followed by the word for hundred. Hundred."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "百。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "It features a dipping and rising tone: Bai. To explicitly state 'One Hundred', we combine them. One Hundred."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "一百。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Notice how the tone of 'Yi' shifts slightly when paired: Yibai. Repeat out loud. One Hundred."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "一百。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 1: MIXED NUMBERS)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "You have unlocked the basic numeric grid. Let's launch into our deep-recall loop. I will fire numbers at random. Translate into Chinese instantly. Eight."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "八。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Zero."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "零。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Four."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "四。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "One Hundred."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "一百。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Six."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "六。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Two."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "二。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Ten."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "十。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 2: CROSS-TOPIC BRIDGING)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Excellent. Now we bridge topics. This block introduces past vocabulary from Lesson 1 alongside your numbers. Do not get caught off guard. Say: Nine."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "九。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Now say: Hello."
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
        "text": "Say: Three."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "三。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Thank you."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Seven."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "七。"
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
        "text": "Say: Five."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "五。"
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
        "voice": "female",
        "text": "对。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Perfect execution. Your ability to shift seamlessly between conversational placeholders and numeric variables is locking into long-term memory. End of Lesson 2."
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
    mp3_path = r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson2.mp3"

    combined.export(mp3_path, format="mp3")

    # Export timestamps JSON
    json_path = r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson2.json"

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
