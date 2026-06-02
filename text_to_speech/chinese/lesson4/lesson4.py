import asyncio
import edge_tts
from pydub import AudioSegment

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
        "voice": "narrator",
        "text": "Welcome to Level 1, Topic 4 of your Chinese Audio Coach. Today we handle spatial orientation and navigation. Navigating an intersection or asking a taxi driver for assistance relies on flawless directional signaling. Speak your responses out loud during the pauses. Let's start with 'Where'."
    },
    {
        "voice": "male",
        "text": "在哪儿？"
    },
    {
        "voice": "narrator",
        "text": "Notice the tongue-curl at the end of the phrase: Zài nǎr? Where is it located? Listen again."
    },
    {
        "voice": "female",
        "text": "在哪儿？"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Where?"
    },
    {
        "voice": "male",
        "text": "在哪儿？"
    },
    {
        "pause": 2000 
    },

    # =========================================================
    # MODULE 1: BASIC NAVIGATIONAL STEERING
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's learn how to direct a driver. To tell someone to go straight ahead, a native speaker says."
    },
    {
        "voice": "female",
        "text": "一直走。"
    },
    {
        "voice": "narrator",
        "text": "Listen to the rising tone shifting into a dipping tone: Yìzhí zǒu. Go straight ahead. Listen again."
    },
    {
        "voice": "male",
        "text": "一直走。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Go straight ahead."
    },
    {
        "voice": "female",
        "text": "一直走。"
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "To tell someone to stop or pull over, use this crisp command: Stop."
    },
    {
        "voice": "male",
        "text": "停。"
    },
    {
        "voice": "narrator",
        "text": "A rising tone, like a quick signal flare: Tíng. Stop."
    },
    {
        "voice": "female",
        "text": "停。"
    },
    {
        "voice": "narrator",
        "text": "Your turn to speak. Stop."
    },
    {
        "voice": "male",
        "text": "停。"
    },
    {
        "pause": 1500
    },

    # =========================================================
    # RECALL BLOCK A: ACTION COMMANDS
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's anchor these action variables instantly. Translate during the silence. Go straight ahead."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "一直走。"
    },
    {
        "voice": "narrator",
        "text": "Where is it located?"
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "在哪儿？"
    },
    {
        "voice": "narrator",
        "text": "Stop."
    },
    {
        "pause": 1500
    },
    {
        "voice": "female",
        "text": "停。"
    },

    # =========================================================
    # MODULE 2: LEFT, RIGHT, AND TURNING MECHANICS
    # =========================================================
    {
        "voice": "narrator",
        "text": "Moving to Module 2. Let's master turning. First, the spatial coordinate for 'Left side'."
    },
    {
        "voice": "male",
        "text": "左边。"
    },
    {
        "voice": "narrator",
        "text": "The first syllable dips low: Zuǒbiān. Left side."
    },
    {
        "voice": "female",
        "text": "左边。"
    },
    {
        "voice": "narrator",
        "text": "Now, the spatial coordinate for 'Right side'."
    },
    {
        "voice": "male",
        "text": "右边。"
    },
    {
        "voice": "narrator",
        "text": "The first syllable drops down hard: Yòubiān. Right side."
    },
    {
        "voice": "female",
        "text": "右边。"
    },
    {
        "voice": "narrator",
        "text": "To say 'Turn', we use the word 'guǎi'. Let's combine them to create: Turn left."
    },
    {
        "voice": "male",
        "text": "左拐。"
    },
    {
        "voice": "narrator",
        "text": "Listen to how the tones bounce: Zuǒ guǎi. Turn left."
    },
    {
        "voice": "female",
        "text": "左拐。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Turn left."
    },
    {
        "voice": "male",
        "text": "左拐。"
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "Now combine the words to create: Turn right."
    },
    {
        "voice": "female",
        "text": "右拐。"
    },
    {
        "voice": "narrator",
        "text": "Listen to the sharp drop on the first word: Yòu guǎi. Turn right."
    },
    {
        "voice": "male",
        "text": "右拐。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Turn right."
    },
    {
        "voice": "female",
        "text": "右拐。"
    },
    {
        "pause": 2000
    },

    # =========================================================
    # RECALL BLOCK B: SPATIAL VECTOR MATRIX
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's drill these spatial vectors. Stay sharp and respond instantly. Left side."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "左边。"
    },
    {
        "voice": "narrator",
        "text": "Turn right."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "右拐。"
    },
    {
        "voice": "narrator",
        "text": "Right side."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "右边。"
    },
    {
        "voice": "narrator",
        "text": "Turn left."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "左拐。"
    },
    {
        "voice": "narrator",
        "text": "Go straight ahead."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "一直走。"
    },

    # =========================================================
    # MODULE 3: THE HIGHWAY CHOPPED MAP (FRONT AND BACK)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Module 3 introduces your final front and back boundary markers. To indicate the 'Front' or 'Ahead', say."
    },
    {
        "voice": "female",
        "text": "前面。"
    },
    {
        "voice": "narrator",
        "text": "A rising tone followed by a falling tone: Qiánmiàn. Front."
    },
    {
        "voice": "male",
        "text": "前面。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. In front."
    },
    {
        "voice": "female",
        "text": "前面。"
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "To indicate the 'Back' or 'Behind', say."
    },
    {
        "voice": "male",
        "text": "后面。"
    },
    {
        "voice": "narrator",
        "text": "A sharp dropping tone followed by another dropping tone: Hòumiàn. Behind."
    },
    {
        "voice": "female",
        "text": "后面。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Behind."
    },
    {
        "voice": "male",
        "text": "后面。"
    },
    {
        "pause": 2000
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 1: DIRECTIONS GRID)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Direction modules are complete. Let's enter the integrated review grid. Say the terms clearly. Behind."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "后面。"
    },
    {
        "voice": "narrator",
        "text": "Turn left."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "左拐。"
    },
    {
        "voice": "narrator",
        "text": "In front."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "前面。"
    },
    {
        "voice": "narrator",
        "text": "Where is it?"
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "在哪儿？"
    },
    {
        "voice": "narrator",
        "text": "Turn right."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "右拐。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 2: QUAD-TOPIC INTEGRATION BRIDGE)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Incredible. Now, prepare for the ultimate test. We are bridging vocabulary from Lesson 1 greetings, Lesson 2 and 3 numbers, and today's navigation. Do not slow down. Say: Hello (formal)."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "您好。"
    },
    {
        "voice": "narrator",
        "text": "Say: Turn right."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "右拐。"
    },
    {
        "voice": "narrator",
        "text": "Say: How much money?"
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "多少钱？"
    },
    {
        "voice": "narrator",
        "text": "Say: Two Dollars."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "两块。"
    },
    {
        "voice": "narrator",
        "text": "Say: Go straight ahead."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "一直走。"
    },
    {
        "voice": "narrator",
        "text": "Say: Thank you."
    },
    {
        "pause": 1500
    },
    {
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "voice": "narrator",
        "text": "Say: Six."
    },
    {
        "pause": 1500
    },
    {
        "voice": "male",
        "text": "六。"
    },
    {
        "voice": "narrator",
        "text": "Say: Stop."
    },
    {
        "pause": 1500
    },
    {
        "voice": "female",
        "text": "停。"
    },
    {
        "voice": "narrator",
        "text": "Say: Goodbye."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "再见。"
    },
    {
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

    for idx, item in enumerate(script):

        # Handle pauses
        if "pause" in item:
            silence = AudioSegment.silent(duration=item["pause"])
            combined += silence
            continue

        voice = get_voice(item["voice"])
        text = item["text"]

        filename = f"temp_{idx}.mp3"

        print(f"Generating: {text[:40]}")

        await generate_tts(text, voice, filename)

        segment = AudioSegment.from_mp3(filename)

        combined += segment

        # Small natural pause between clips
        combined += AudioSegment.silent(duration=500)

    # Export final lesson
    combined.export(r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson4.mp3", format="mp3")

    print("Finished! Saved as lesson4.mp3")
    


# =========================
# RUN
# =========================

asyncio.run(build_lesson())