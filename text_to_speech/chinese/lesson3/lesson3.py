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
    # INTRODUCTION & THE RULE OF TWO
    # =========================================================
    {
        "voice": "narrator",
        "text": "Welcome to Level 1, Topic 3 of your Chinese Audio Coach. Today we handle advanced numbers, massive counting scales, and currency. First, we must master a critical rule. When counting physical items or specifying 'two' of something, Chinese switches from èr to a completely different word. Listen closely."
    },
    {
        "voice": "male",
        "text": "两。"
    },
    {
        "voice": "narrator",
        "text": "Notice the dipping and rising tone: Liǎng. Use this for two people, two hours, or two dollars. Never use èr for quantities. Listen again."
    },
    {
        "voice": "female",
        "text": "两。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Two of something."
    },
    {
        "voice": "male",
        "text": "两。"
    },
    {
        "pause": 2000 
    },

    # =========================================================
    # MODULE 1: THOUSANDS & TEN-THOUSANDS (THE LINGUISTIC SHIFT)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Now let's scale up. To say Thousand, we use a sharp dropping tone. Thousand."
    },
    {
        "voice": "female",
        "text": "千。"
    },
    {
        "voice": "narrator",
        "text": "Pronounced high and flat: Qiān. Let's make it One Thousand."
    },
    {
        "voice": "male",
        "text": "一千。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. One Thousand."
    },
    {
        "voice": "female",
        "text": "一千。"
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "Unlike English which groups numbers by thousands, Chinese groups large numbers by four digits—meaning ten-thousand gets its own unique base word. Ten-Thousand."
    },
    {
        "voice": "male",
        "text": "万。"
    },
    {
        "voice": "narrator",
        "text": "A sharp, definitive falling tone: Wàn. Let's say One Ten-Thousand."
    },
    {
        "voice": "female",
        "text": "一万。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Ten Thousand."
    },
    {
        "voice": "male",
        "text": "一万。"
    },
    {
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK A: SCALE FOUNDATIONS
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's pause and anchor these base scales. Speak your answers instantly. One Thousand."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "一千。"
    },
    {
        "voice": "narrator",
        "text": "Ten Thousand."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "一万。"
    },
    {
        "voice": "narrator",
        "text": "How do you say 'two' when counting physical objects?"
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "两。"
    },
    {
        "voice": "narrator",
        "text": "One Hundred from our previous lesson."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "一百。"
    },

    # =========================================================
    # MODULE 2: MILLIONS & CASH TERMINOLOGY
    # =========================================================
    {
        "voice": "narrator",
        "text": "Moving to Module 2. Because of the four-digit grouping system, One Million is expressed literally as 'One Hundred Ten-Thousands'. One Million."
    },
    {
        "voice": "female",
        "text": "一百万。"
    },
    {
        "voice": "narrator",
        "text": "Listen to the compounding blocks: Yì bǎi wàn. One Million."
    },
    {
        "voice": "male",
        "text": "一百万。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. One Million."
    },
    {
        "voice": "female",
        "text": "一百万。"
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "Now let's talk money. The formal name for Chinese currency is the Renminbi, but in daily life, people use the word for 'piece' or 'bucket' to count money. Dollar."
    },
    {
        "voice": "male",
        "text": "块。"
    },
    {
        "voice": "narrator",
        "text": "A strong, falling tone: Kuài. Let's combine it with our new quantity rule to say Two Dollars."
    },
    {
        "voice": "female",
        "text": "两块。"
    },
    {
        "voice": "narrator",
        "text": "Notice it uses liǎng, never èr. Two Dollars."
    },
    {
        "voice": "male",
        "text": "两块。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Two Dollars."
    },
    {
        "voice": "female",
        "text": "两块。"
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "To ask 'How much money is it?' when shopping, a native speaker says."
    },
    {
        "voice": "male",
        "text": "多少钱？"
    },
    {
        "voice": "narrator",
        "text": "Listen to the cadence: Duōshǎo qián? How much money? Listen again."
    },
    {
        "voice": "female",
        "text": "多少钱？"
    },
    {
        "voice": "narrator",
        "text": "Repeat this essential shopping phrase. How much money?"
    },
    {
        "voice": "male",
        "text": "多少钱？"
    },
    {
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK B: ADVANCED COMBINATIONS
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's drill these financial patterns. Give me the Chinese translation during the silence. Two Dollars."
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
        "text": "How much money?"
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
        "text": "One Million."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "一百万。"
    },
    {
        "voice": "narrator",
        "text": "Ten Dollars."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "十块。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 1: ADVANCED NUMBERS)
    # =========================================================
    {
        "voice": "narrator",
        "text": "You have unlocked the full core numeric scaling grid. Let's enter the deep-retention challenge loop. Translate the advanced metrics instantly. One Thousand."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "一千。"
    },
    {
        "voice": "narrator",
        "text": "How much money?"
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
        "text": "Two of something."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "两。"
    },
    {
        "voice": "narrator",
        "text": "Ten Thousand."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "一万。"
    },
    {
        "voice": "narrator",
        "text": "Two Dollars."
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
        "text": "One Million."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "一百万。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 2: DEEP LESSONS 1-3 CROSS BRIDGE)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Phenomenal. Now we execute an ultimate triple-topic integration drill. This combines greetings, primary numbers, and transaction scales. Stay highly responsive. Say: Hello."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "你好。"
    },
    {
        "voice": "narrator",
        "text": "Say: Eight Dollars."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "八块。"
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
        "text": "Say: Five Thousand."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "五千。"
    },
    {
        "voice": "narrator",
        "text": "Say: Goodbye."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "再见。"
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
        "text": "Say: I'm sorry."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "对不起。"
    },
    {
        "voice": "narrator",
        "text": "Say: Two (the digit used for counting math, not objects)."
    },
    {
        "pause": 1500
    },
    {
        "voice": "male",
        "text": "二。"
    },
    {
        "voice": "narrator",
        "text": "Say: Two Dollars (using the quantity format)."
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
        "text": "Say: Correct."
    },
    {
        "pause": 1500
    },
    {
        "voice": "male",
        "text": "对。"
    },
    {
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
    combined.export("topic1_lesson.mp3", format="mp3")

    print("Finished! Saved as topic1_lesson.mp3")
    


# =========================
# RUN
# =========================

asyncio.run(build_lesson())