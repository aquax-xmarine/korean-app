import asyncio
import edge_tts
from pydub import AudioSegment
import json
import re

# =========================
# VOICE CONFIGURATION
# =========================

NARRATOR_VOICE = "en-US-AvaMultilingualNeural"
CHINESE_MALE = "zh-CN-YunxiNeural"
CHINESE_FEMALE = "zh-CN-XiaoxiaoNeural"

# =========================
# LESSON SCRIPT
# =========================

VOCABULARY = {
    "在哪儿": {
        "pinyin": "zài nǎr",
        "english": "where"
    },
    "一直走": {
        "pinyin": "yìzhí zǒu",
        "english": "go straight ahead"
    },
    "停": {
        "pinyin": "tíng",
        "english": "stop"
    },
    "左边": {
        "pinyin": "zuǒ biān",
        "english": "left side"
    },
    "右边": {
        "pinyin": "yòu biān",
        "english": "right side"
    },
    "左拐": {
        "pinyin": "zuǒ guǎi",
        "english": "turn left"
    },
    "右拐": {
        "pinyin": "yòu guǎi",
        "english": "turn right"
    },
    "前面": {
        "pinyin": "qián miàn",
        "english": "front"
    },
    "后面": {
        "pinyin": "hòu miàn",
        "english": "behind"
    },
    "您好": {
        "pinyin": "nín hǎo",
        "english": "hello (formal)"
    },
    "多少钱": {
        "pinyin": "duō shǎo qián",
        "english": "how much money"
    },
    "两块": {
        "pinyin": "liǎng kuài",
        "english": "two dollars"
    },
    "谢谢": {
        "pinyin": "xiè xie",
        "english": "thank you"
    },
    "六": {
        "pinyin": "liù",
        "english": "six"
    },
    "再见": {
        "pinyin": "zài jiàn",
        "english": "goodbye"
    }
}

script = [
    # =========================================================
    # INTRODUCTION
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Welcome to Level 1, Topic 4 of your Chinese Audio Coach. Today we handle spatial orientation and navigation. Navigating an intersection or asking a taxi driver for assistance relies on flawless directional signaling. Speak your responses out loud during the pauses. Let's start with 'Where'."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "在哪儿？"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Notice the tongue-curl at the end of the phrase: Zài nǎr? Where is it located? Listen again."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "在哪儿？"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Where?"
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "在哪儿？"
    },
    {
        "section": "teaching",
        "pause": 2000
    },

    # =========================================================
    # MODULE 1: BASIC NAVIGATIONAL STEERING
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Let's learn how to direct a driver. To tell someone to go straight ahead, a native speaker says."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "一直走。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the rising tone shifting into a dipping tone: Yìzhí zǒu. Go straight ahead. Listen again."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "一直走。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Go straight ahead."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "一直走。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "To tell someone to stop or pull over, use this administrative command: Stop."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "停。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "A rising tone, like a quick signal flare: Tíng. Stop."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "停。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Your turn to speak. Stop."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "停。"
    },
    {
        "section": "teaching",
        "pause": 1500
    },

    # =========================================================
    # RECALL BLOCK A: ACTION COMMANDS
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Let's anchor these action variables instantly. Translate during the silence. Go straight ahead."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "一直走。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Where is it located?"
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "在哪儿？"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Stop."
    },
    {
        "section": "review",
        "pause": 1500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "停。"
    },

    # =========================================================
    # MODULE 2: LEFT, RIGHT, AND TURNING MECHANICS
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Moving to Module 2. Let's master turning. First, the spatial coordinate for 'Left side'."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "左边。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "The first syllable dips low: Zuǒbiān. Left side."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "左边。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Now, the spatial coordinate for 'Right side'."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "右边。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "The first syllable drops down hard: Yòubiān. Right side."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "右边。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "To say 'Turn', we use the word 'guǎi'. Let's combine them to create: Turn left."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "左拐。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to how the tones bounce: Zuǒ guǎi. Turn left."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "左拐。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Turn left."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "左拐。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Now combine the words to create: Turn right."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "右拐。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the sharp drop on the first word: Yòu guǎi. Turn right."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "右拐。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Turn right."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "右拐。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },

    # =========================================================
    # RECALL BLOCK B: SPATIAL VECTOR MATRIX
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Let's drill these spatial vectors. Stay sharp and respond instantly. Left side."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "左边。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Turn right."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "右拐。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Right side."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "右边。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Turn left."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "左拐。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Go straight ahead."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "一直走。"
    },

    # =========================================================
    # MODULE 3: THE HIGHWAY CHOPPED MAP (FRONT AND BACK)
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Module 3 introduces your final front and back boundary markers. To indicate the 'Front' or 'Ahead', say."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "前面。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "A rising tone followed by a falling tone: Qiánmiàn. Front."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "前面。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. In front."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "前面。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "To indicate the 'Back' or 'Behind', say."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "后面。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "A sharp dropping tone followed by another dropping tone: Hòumiàn. Behind."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "后面。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Behind."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "后面。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 1: DIRECTIONS GRID)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Direction modules are complete. Let's enter the integrated review grid. Say the terms clearly. Behind."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "后面。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Turn left."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "左拐。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "In front."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "前面。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Where is it?"
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "在哪儿？"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Turn right."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "右拐。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 2: QUAD-TOPIC INTEGRATION BRIDGE)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Incredible. Now, prepare for the ultimate test. We are bridging vocabulary from Lesson 1 greetings, Lesson 2 and 3 numbers, and today's navigation. Do not slow down. Say: Hello (formal)."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "您好。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Turn right."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "右拐。"
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
        "text": "Say: Two Dollars."
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
        "text": "Say: Go straight ahead."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "一直走。"
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
        "text": "Say: Six."
    },
    {
        "section": "review",
        "pause": 1500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "六。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: Stop."
    },
    {
        "section": "review",
        "pause": 1500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "停。"
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
        "voice": "male",
        "text": "再见。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Absolute mastery. You have effortlessly linked conversational courtesy, complex financial values, and immediate situational geometry. Class dismissed."
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

        # Save timestamps only for Chinese phrases
        if re.search(r'[\u4e00-\u9fff]', text):

            timestamps.append({
                "text": clean_text,
                "pinyin": VOCABULARY.get(clean_text, {}).get("pinyin", ""),
                "english": VOCABULARY.get(clean_text, {}).get("english", ""),
                "section": item["section"],
                "start": round(current_ms / 1000, 2),
                "end": round((current_ms + duration) / 1000, 2)
            })

        combined += segment

        current_ms += duration

        # Natural pause
        combined += AudioSegment.silent(duration=500)

        current_ms += 500

    # Export MP3
    mp3_path = r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson4.mp3"

    combined.export(mp3_path, format="mp3")

    # Export timestamps JSON
    json_path = r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson4.json"

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
