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
        "text": "Welcome to Level 1, Topic 1 of your Chinese Audio Coach. Mandarin Chinese is a tonal language, meaning pitch changes word meanings. Listen carefully, mimic the music of the language, and speak out loud during the pauses. Let's begin."
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Imagine meeting someone for the first time in Beijing. To say a standard, polite hello, a native speaker says."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "你好。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Notice the dip and rise in pitch. Both syllables drop then rise. When spoken together, the first syllable softens slightly. Listen again."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "你好。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Now repeat out loud after the speaker. Match their pitch. Hello."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "你好。"
    },
    {
        "section": "teaching",
        "pause": 2000 
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Try saying it again. Hello."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "你好。"
    },
    {
        "section": "teaching",
        "pause": 2000 
    },

    # =========================================================
    # MODULE 1: POLITE VARIATIONS & TIME OF DAY
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "If you are addressing an elder, a teacher, or a client, you should use the formal, respectful version of you. Hello (formal)."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "您好。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the subtle nasal 'n' sound added to the first syllable: Nín hǎo. Formal hello."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "您好。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Your turn. Speak out loud. Hello (formal)."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "您好。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Now, let's learn how to greet someone in the morning. A native speaker says: Good morning."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "早上好。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the sharp, clear tones. Good morning."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "早上好。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud after the speaker."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "早上好。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Say it one more time. Good morning."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "早上好。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "At night, before someone goes to sleep or when parting ways late, you say: Good night."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "晚安。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat after the male speaker. Good night."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "晚安。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK A: GREETINGS REPETITION
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Let's test your memory. Say the Chinese translation during the pause. Hello (standard)."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "你好。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say it again. Hello."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "你好。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "How do you say 'Hello' formally to an older person?"
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
        "text": "Now tell someone good morning."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "早上好。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "And wish them a peaceful good night."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "晚安。"
    },

    # =========================================================
    # MODULE 2: GRATITUDE & RESPONSES
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Moving to Module 2: Expressing gratitude. To thank someone, a native speaker says."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Notice how the second syllable drops off sharply and becomes quiet: Xièxie. Listen again."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "谢谢。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Thank you."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "When someone thanks you, respond politely with 'You're welcome'. The traditional phrase literally means 'No need to be polite'."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "不客气。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the female speaker. You're welcome."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "不客气。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. You're welcome."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "不客气。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Another common way to say 'You’re welcome' or 'Don't mention it' is: No need to thank."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "不用谢。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat. No need for thanks."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "不用谢。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },

    # =========================================================
    # RECALL BLOCK B: ALL PREVIOUS TOPICS (MODULE 1 + MODULE 2)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Time for a cumulative review. Speed is key. How do you say Thank you?"
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "How do you say Hello standard?"
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "你好。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Respond to thank you with 'You're welcome'."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "不客气。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Greet a boss or an elder. Formal hello."
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
        "text": "Say 'Don't mention it' or 'No need for thanks'."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "不用谢。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Finally, wish someone a good morning."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "早上好。"
    },

    # =========================================================
    # MODULE 3: AGREEMENT, DISAGREEMENT & APOLOGIES
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Module 3 handles basic validation, answers, and mistakes. To say 'Correct' or 'Yes' in response to a statement, we say."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "对。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "It is a short, sharp downward tone: Duì. Correct."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "对。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat it now. Correct."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "对。"
    },
    {
        "section": "teaching",
        "pause": 1500
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "To negate or say 'No/Not correct', add the word for 'Not' in front. Not correct."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "不对。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat the negative. Incorrect."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "不对。"
    },
    {
        "section": "teaching",
        "pause": 1500
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "If you make a mistake, apologize politely. I'm sorry."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "对不起。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen again. Notice the bouncy rhythm. Duìbuqǐ."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "对不起。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Your turn to speak. I'm sorry."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "对不起。"
    },
    {
        "section": "teaching",
        "pause": 2000
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "When someone apologizes to you, reassure them by saying 'It's okay' or 'It doesn't matter'."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "没关系。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the smooth flow: Méi guānxi. It's okay."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "没关系。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. It doesn't matter."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "没关系。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK C: ALL PREVIOUS TOPICS (MODULES 1, 2, + 3)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Let's perform a comprehensive review loop. Answer fast. Say: Correct."
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
        "text": "Say: Incorrect."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "不对。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: I'm sorry."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "对不起。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Say: It's okay / It doesn't matter."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "没关系。"
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
        "text": "Say: Good night."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "晚安。"
    },

    # =========================================================
    # MODULE 4: COURTESY, MEETINGS & FAREWELLS
    # =========================================================
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "In Module 4, let's learn how to ask for something politely. To say 'Please' or 'Excuse me' before an action, say."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "请。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "It dips down and comes up: Qǐng. Please."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "请。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat out loud. Please."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "请。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "When meeting someone for the first time, express your joy. Nice to meet you."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "很高兴认识你。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Listen to the breakdown: Hěn gāoxìng rènshi nǐ. Very glad to know you. Listen again."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "很高兴认识你。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Try repeating this longer phrase carefully. Nice to meet you."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "很高兴认识你。"
    },
    {
        "section": "teaching",
        "pause": 3000
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Finally, when it is time to part ways, say goodbye. Goodbye."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "再见。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Both words drop hard down in pitch: Zàijiàn. It literally means 'See you again'. Listen again."
    },
    {
        "section": "teaching",
        "voice": "male",
        "text": "再见。"
    },
    {
        "section": "teaching",
        "voice": "narrator",
        "text": "Repeat clearly. Goodbye."
    },
    {
        "section": "teaching",
        "voice": "female",
        "text": "再见。"
    },
    {
        "section": "teaching",
        "pause": 2500
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 1)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "You have unlocked the core structures. Let's enter the comprehensive retention challenge loop. Speak your answers instantly during the silence. Good morning."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "早上好。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Thank you."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "It doesn't matter / It's okay."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "没关系。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Please."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "请。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Nice to meet you."
    },
    {
        "section": "review",
        "pause": 3000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "很高兴认识你。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Hello (formal version)."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "您好。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Goodbye."
    },
    {
        "section": "review",
        "pause": 2500
    },
    {
        "section": "review",
        "voice": "male",
        "text": "再见。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 2 - SPEED ROUND)
    # =========================================================
    {
        "section": "review",
        "voice": "narrator",
        "text": "Final accelerated round to establish effortless recall. Keep your energy up. Hello."
    },
    {
        "section": "review",
        "pause": 1500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "你好。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Correct."
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
        "text": "Incorrect."
    },
    {
        "section": "review",
        "pause": 1500
    },
    {
        "section": "review",
        "voice": "female",
        "text": "不对。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "I'm sorry."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "对不起。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "You're welcome."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "female",
        "text": "不客气。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Good night."
    },
    {
        "section": "review",
        "pause": 2000
    },
    {
        "section": "review",
        "voice": "male",
        "text": "晚安。"
    },
    {
        "section": "review",
        "voice": "narrator",
        "text": "Excellent work. Your muscle memory for foundational Mandarin greetings is now operating automatically. Keep practicing out loud. Session complete."
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
    mp3_path = r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson1.mp3"

    combined.export(mp3_path, format="mp3")

    # Export timestamps JSON
    json_path = r"C:\Users\NIKISHA\Documents\korean-app\frontend\public\assets\audio\chinese\lesson1.json"

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
