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
        "text": "Welcome to Level 1, Topic 2 of your Chinese Audio Coach. Today we are mastering numbers. Chinese numbers follow a beautifully logical pattern, but you must nail the tones to be understood. Speak out loud during every pause. Let's start with zero."
    },
    {
        "voice": "male",
        "text": "零。"
    },
    {
        "voice": "narrator",
        "text": "Notice the rising tone, like asking a question: Ling. Zero."
    },
    {
        "voice": "female",
        "text": "零。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Zero."
    },
    {
        "voice": "male",
        "text": "零。"
    },
    {
        "pause": 2000 
    },

    # =========================================================
    # MODULE 1: NUMBERS 1 TO 3
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's build the first sequence. The number One is a flat, high pitch. One."
    },
    {
        "voice": "female",
        "text": "一。"
    },
    {
        "voice": "narrator",
        "text": "Keep your pitch high and steady: Yi. One."
    },
    {
        "voice": "male",
        "text": "一。"
    },
    {
        "voice": "narrator",
        "text": "The number Two is a sharp, dropping tone. Two."
    },
    {
        "voice": "female",
        "text": "二。"
    },
    {
        "voice": "narrator",
        "text": "Drop your pitch with confidence: Èr. Two."
    },
    {
        "voice": "male",
        "text": "二。"
    },
    {
        "voice": "narrator",
        "text": "The number Three returns to a high, flat pitch. Three."
    },
    {
        "voice": "female",
        "text": "三。"
    },
    {
        "voice": "narrator",
        "text": "Listen to the steady energy: San. Three."
    },
    {
        "voice": "male",
        "text": "三。"
    },
    {
        "voice": "narrator",
        "text": "Now, repeat the sequence one through three after the speaker. One, Two, Three."
    },
    {
        "voice": "female",
        "text": "一，二，三。"
    },
    {
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK A: 0 TO 3 REPETITION
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's check your foundation. Say the Chinese numbers instantly during the pauses. Zero."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "零。"
    },
    {
        "voice": "narrator",
        "text": "Three."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "三。"
    },
    {
        "voice": "narrator",
        "text": "One."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "一。"
    },
    {
        "voice": "narrator",
        "text": "Two."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "二。"
    },

    # =========================================================
    # MODULE 2: NUMBERS 4 TO 6
    # =========================================================
    {
        "voice": "narrator",
        "text": "Moving to Module 2. The number Four is a sharp downward tone, hitting a crisp 's' sound. Four."
    },
    {
        "voice": "male",
        "text": "四。"
    },
    {
        "voice": "narrator",
        "text": "Make it short and punchy: Si. Four."
    },
    {
        "voice": "female",
        "text": "四。"
    },
    {
        "voice": "narrator",
        "text": "The number Five scoop downwards and climbs back up. Five."
    },
    {
        "voice": "male",
        "text": "五。"
    },
    {
        "voice": "narrator",
        "text": "Let your pitch dip low: Wu. Five."
    },
    {
        "voice": "female",
        "text": "五。"
    },
    {
        "voice": "narrator",
        "text": "The number Six drops sharply. Six."
    },
    {
        "voice": "male",
        "text": "六。"
    },
    {
        "voice": "narrator",
        "text": "Pronounced like 'liou' with a falling pitch: Liu. Six."
    },
    {
        "voice": "female",
        "text": "六。"
    },
    {
        "voice": "narrator",
        "text": "Now challenge yourself. Repeat four, five, six."
    },
    {
        "voice": "male",
        "text": "四，五，六。"
    },
    {
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK B: CUMULATIVE 0 TO 6
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's combine both blocks. Keep your focus sharp. Say: Four."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "四。"
    },
    {
        "voice": "narrator",
        "text": "Two."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "二。"
    },
    {
        "voice": "narrator",
        "text": "Five."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "五。"
    },
    {
        "voice": "narrator",
        "text": "Three."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "三。"
    },
    {
        "voice": "narrator",
        "text": "Six."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "六。"
    },
    {
        "voice": "narrator",
        "text": "One."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "一。"
    },

    # =========================================================
    # MODULE 3: NUMBERS 7 TO 10
    # =========================================================
    {
        "voice": "narrator",
        "text": "Module 3 finishes the base sequence. The number Seven is high and flat. Seven."
    },
    {
        "voice": "female",
        "text": "七。"
    },
    {
        "voice": "narrator",
        "text": "Keep it high and thin: Qi. Seven."
    },
    {
        "voice": "male",
        "text": "七。"
    },
    {
        "voice": "narrator",
        "text": "The number Eight is also high and flat. In Chinese culture, this is the luckiest number. Eight."
    },
    {
        "voice": "female",
        "text": "八。"
    },
    {
        "voice": "narrator",
        "text": "High and level pitch: Ba. Eight."
    },
    {
        "voice": "male",
        "text": "八。"
    },
    {
        "voice": "narrator",
        "text": "The number Nine dips deeply before rising. Nine."
    },
    {
        "voice": "female",
        "text": "九。"
    },
    {
        "voice": "narrator",
        "text": "Scoop your pitch low: Jiu. Nine."
    },
    {
        "voice": "male",
        "text": "九。"
    },
    {
        "voice": "narrator",
        "text": "The number Ten climbs steadily upward. Ten."
    },
    {
        "voice": "female",
        "text": "十。"
    },
    {
        "voice": "narrator",
        "text": "Rise from low to high, curling your tongue slightly: Shi. Ten."
    },
    {
        "voice": "male",
        "text": "十。"
    },
    {
        "voice": "narrator",
        "text": "Let's lock in seven through ten. Repeat out loud."
    },
    {
        "voice": "female",
        "text": "七，八，九，十。"
    },
    {
        "pause": 3000
    },

    # =========================================================
    # RECALL BLOCK C: CUMULATIVE 0 TO 10
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's consolidate the entire structure from zero to ten. Stay loose and match the tones. Say: Ten."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "十。"
    },
    {
        "voice": "narrator",
        "text": "Seven."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "七。"
    },
    {
        "voice": "narrator",
        "text": "Eight."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "八。"
    },
    {
        "voice": "narrator",
        "text": "Nine."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "九。"
    },
    {
        "voice": "narrator",
        "text": "Five."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "五。"
    },
    {
        "voice": "narrator",
        "text": "Zero."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "零。"
    },

    # =========================================================
    # MODULE 4: HUNDRED & LESSON 1 RECALL BRIDGING
    # =========================================================
    {
        "voice": "narrator",
        "text": "In Module 4, let's look at how to expand your scope. To say 'One Hundred', we use the word for one, followed by the word for hundred. Hundred."
    },
    {
        "voice": "male",
        "text": "百。"
    },
    {
        "voice": "narrator",
        "text": "It features a dipping and rising tone: Bai. To explicitly state 'One Hundred', we combine them. One Hundred."
    },
    {
        "voice": "female",
        "text": "一百。"
    },
    {
        "voice": "narrator",
        "text": "Notice how the tone of 'Yi' shifts slightly when paired: Yibai. Repeat out loud. One Hundred."
    },
    {
        "voice": "male",
        "text": "一百。"
    },
    {
        "pause": 2500
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 1: MIXED NUMBERS)
    # =========================================================
    {
        "voice": "narrator",
        "text": "You have unlocked the basic numeric grid. Let's launch into our deep-recall loop. I will fire numbers at random. Translate into Chinese instantly. Eight."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "八。"
    },
    {
        "voice": "narrator",
        "text": "Zero."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "零。"
    },
    {
        "voice": "narrator",
        "text": "Four."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "四。"
    },
    {
        "voice": "narrator",
        "text": "One Hundred."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "一百。"
    },
    {
        "voice": "narrator",
        "text": "Six."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "六。"
    },
    {
        "voice": "narrator",
        "text": "Two."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "二。"
    },
    {
        "voice": "narrator",
        "text": "Ten."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "十。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 2: CROSS-TOPIC BRIDGING)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Excellent. Now we bridge topics. This block introduces past vocabulary from Lesson 1 alongside your numbers. Do not get caught off guard. Say: Nine."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "九。"
    },
    {
        "voice": "narrator",
        "text": "Now say: Hello."
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
        "text": "Say: Three."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "三。"
    },
    {
        "voice": "narrator",
        "text": "Say: Thank you."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "voice": "narrator",
        "text": "Say: Seven."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "七。"
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
        "text": "Say: Five."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "五。"
    },
    {
        "voice": "narrator",
        "text": "Say: Correct."
    },
    {
        "pause": 1500
    },
    {
        "voice": "female",
        "text": "对。"
    },
    {
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