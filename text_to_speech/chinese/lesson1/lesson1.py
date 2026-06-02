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
        "text": "Welcome to Level 1, Topic 1 of your Chinese Audio Coach. Mandarin Chinese is a tonal language, meaning pitch changes word meanings. Listen carefully, mimic the music of the language, and speak out loud during the pauses. Let's begin."
    },
    {
        "voice": "narrator",
        "text": "Imagine meeting someone for the first time in Beijing. To say a standard, polite hello, a native speaker says."
    },
    {
        "voice": "male",
        "text": "你好。"
    },
    {
        "voice": "narrator",
        "text": "Notice the dip and rise in pitch. Both syllables drop then rise. When spoken together, the first syllable softens slightly. Listen again."
    },
    {
        "voice": "female",
        "text": "你好。"
    },
    {
        "voice": "narrator",
        "text": "Now repeat out loud after the speaker. Match their pitch. Hello."
    },
    {
        "voice": "male",
        "text": "你好。"
    },
    {
        "pause": 2000 
    },
    {
        "voice": "narrator",
        "text": "Try saying it again. Hello."
    },
    {
        "voice": "female",
        "text": "你好。"
    },
    {
        "pause": 2000 
    },

    # =========================================================
    # MODULE 1: POLITE VARIATIONS & TIME OF DAY
    # =========================================================
    {
        "voice": "narrator",
        "text": "If you are addressing an elder, a teacher, or a client, you should use the formal, respectful version of you. Hello (formal)."
    },
    {
        "voice": "male",
        "text": "您好。"
    },
    {
        "voice": "narrator",
        "text": "Listen to the subtle nasal 'n' sound added to the first syllable: Nín hǎo. Formal hello."
    },
    {
        "voice": "female",
        "text": "您好。"
    },
    {
        "voice": "narrator",
        "text": "Your turn. Speak out loud. Hello (formal)."
    },
    {
        "voice": "male",
        "text": "您好。"
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "Now, let's learn how to greet someone in the morning. A native speaker says: Good morning."
    },
    {
        "voice": "female",
        "text": "早上好。"
    },
    {
        "voice": "narrator",
        "text": "Listen to the sharp, clear tones. Good morning."
    },
    {
        "voice": "male",
        "text": "早上好。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud after the speaker."
    },
    {
        "voice": "female",
        "text": "早上好。"
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "Say it one more time. Good morning."
    },
    {
        "voice": "male",
        "text": "早上好。"
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "At night, before someone goes to sleep or when parting ways late, you say: Good night."
    },
    {
        "voice": "female",
        "text": "晚安。"
    },
    {
        "voice": "narrator",
        "text": "Repeat after the male speaker. Good night."
    },
    {
        "voice": "male",
        "text": "晚安。"
    },
    {
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK A: GREETINGS REPETITION
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's test your memory. Say the Chinese translation during the pause. Hello (standard)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "你好。"
    },
    {
        "voice": "narrator",
        "text": "Say it again. Hello."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "你好。"
    },
    {
        "voice": "narrator",
        "text": "How do you say 'Hello' formally to an older person?"
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
        "text": "Now tell someone good morning."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "早上好。"
    },
    {
        "voice": "narrator",
        "text": "And wish them a peaceful good night."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "晚安。"
    },

    # =========================================================
    # MODULE 2: GRATITUDE & RESPONSES
    # =========================================================
    {
        "voice": "narrator",
        "text": "Moving to Module 2: Expressing gratitude. To thank someone, a native speaker says."
    },
    {
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "voice": "narrator",
        "text": "Notice how the second syllable drops off sharply and becomes quiet: Xièxie. Listen again."
    },
    {
        "voice": "male",
        "text": "谢谢。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Thank you."
    },
    {
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "When someone thanks you, respond politely with 'You're welcome'. The traditional phrase literally means 'No need to be polite'."
    },
    {
        "voice": "male",
        "text": "不客气。"
    },
    {
        "voice": "narrator",
        "text": "Listen to the female speaker. You're welcome."
    },
    {
        "voice": "female",
        "text": "不客气。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. You're welcome."
    },
    {
        "voice": "male",
        "text": "不客气。"
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "Another common way to say 'You’re welcome' or 'Don't mention it' is: No need to thank."
    },
    {
        "voice": "female",
        "text": "不用谢。"
    },
    {
        "voice": "narrator",
        "text": "Repeat. No need for thanks."
    },
    {
        "voice": "male",
        "text": "不用谢。"
    },
    {
        "pause": 2000
    },

    # =========================================================
    # RECALL BLOCK B: ALL PREVIOUS TOPICS (MODULE 1 + MODULE 2)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Time for a cumulative review. Speed is key. How do you say Thank you?"
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "voice": "narrator",
        "text": "How do you say Hello standard?"
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "你好。"
    },
    {
        "voice": "narrator",
        "text": "Respond to thank you with 'You're welcome'."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "不客气。"
    },
    {
        "voice": "narrator",
        "text": "Greet a boss or an elder. Formal hello."
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
        "text": "Say 'Don't mention it' or 'No need for thanks'."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "不用谢。"
    },
    {
        "voice": "narrator",
        "text": "Finally, wish someone a good morning."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "早上好。"
    },

    # =========================================================
    # MODULE 3: AGREEMENT, DISAGREEMENT & APOLOGIES
    # =========================================================
    {
        "voice": "narrator",
        "text": "Module 3 handles basic validation, answers, and mistakes. To say 'Correct' or 'Yes' in response to a statement, we say."
    },
    {
        "voice": "male",
        "text": "对。"
    },
    {
        "voice": "narrator",
        "text": "It is a short, sharp downward tone: Duì. Correct."
    },
    {
        "voice": "female",
        "text": "对。"
    },
    {
        "voice": "narrator",
        "text": "Repeat it now. Correct."
    },
    {
        "voice": "male",
        "text": "对。"
    },
    {
        "pause": 1500
    },
    {
        "voice": "narrator",
        "text": "To negate or say 'No/Not correct', add the word for 'Not' in front. Not correct."
    },
    {
        "voice": "female",
        "text": "不对。"
    },
    {
        "voice": "narrator",
        "text": "Repeat the negative. Incorrect."
    },
    {
        "voice": "male",
        "text": "不对。"
    },
    {
        "pause": 1500
    },
    {
        "voice": "narrator",
        "text": "If you make a mistake, apologize politely. I'm sorry."
    },
    {
        "voice": "female",
        "text": "对不起。"
    },
    {
        "voice": "narrator",
        "text": "Listen again. Notice the bouncy rhythm. Duìbuqǐ."
    },
    {
        "voice": "male",
        "text": "对不起。"
    },
    {
        "voice": "narrator",
        "text": "Your turn to speak. I'm sorry."
    },
    {
        "voice": "female",
        "text": "对不起。"
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "When someone apologizes to you, reassure them by saying 'It's okay' or 'It doesn't matter'."
    },
    {
        "voice": "male",
        "text": "没关系。"
    },
    {
        "voice": "narrator",
        "text": "Listen to the smooth flow: Méi guānxi. It's okay."
    },
    {
        "voice": "female",
        "text": "没关系。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. It doesn't matter."
    },
    {
        "voice": "male",
        "text": "没关系。"
    },
    {
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK C: ALL PREVIOUS TOPICS (MODULES 1, 2, + 3)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's perform a comprehensive review loop. Answer fast. Say: Correct."
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
        "text": "Say: Incorrect."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "不对。"
    },
    {
        "voice": "narrator",
        "text": "Say: I'm sorry."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "对不起。"
    },
    {
        "voice": "narrator",
        "text": "Say: It's okay / It doesn't matter."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "没关系。"
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
        "text": "Say: Good night."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "晚安。"
    },

    # =========================================================
    # MODULE 4: COURTESY, MEETINGS & FAREWELLS
    # =========================================================
    {
        "voice": "narrator",
        "text": "In Module 4, let's learn how to ask for something politely. To say 'Please' or 'Excuse me' before an action, say."
    },
    {
        "voice": "female",
        "text": "请。"
    },
    {
        "voice": "narrator",
        "text": "It dips down and comes up: Qǐng. Please."
    },
    {
        "voice": "male",
        "text": "请。"
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Please."
    },
    {
        "voice": "female",
        "text": "请。"
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "When meeting someone for the first time, express your joy. Nice to meet you."
    },
    {
        "voice": "male",
        "text": "很高兴认识你。"
    },
    {
        "voice": "narrator",
        "text": "Listen to the breakdown: Hěn gāoxìng rènshi nǐ. Very glad to know you. Listen again."
    },
    {
        "voice": "female",
        "text": "很高兴认识你。"
    },
    {
        "voice": "narrator",
        "text": "Try repeating this longer phrase carefully. Nice to meet you."
    },
    {
        "voice": "male",
        "text": "很高兴认识你。"
    },
    {
        "pause": 3000
    },
    {
        "voice": "narrator",
        "text": "Finally, when it is time to part ways, say goodbye. Goodbye."
    },
    {
        "voice": "female",
        "text": "再见。"
    },
    {
        "voice": "narrator",
        "text": "Both words drop hard down in pitch: Zàijiàn. It literally means 'See you again'. Listen again."
    },
    {
        "voice": "male",
        "text": "再见。"
    },
    {
        "voice": "narrator",
        "text": "Repeat clearly. Goodbye."
    },
    {
        "voice": "female",
        "text": "再见。"
    },
    {
        "pause": 2500
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 1)
    # =========================================================
    {
        "voice": "narrator",
        "text": "You have unlocked the core structures. Let's enter the comprehensive retention challenge loop. Speak your answers instantly during the silence. Good morning."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "早上好。"
    },
    {
        "voice": "narrator",
        "text": "Thank you."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "谢谢。"
    },
    {
        "voice": "narrator",
        "text": "It doesn't matter / It's okay."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "没关系。"
    },
    {
        "voice": "narrator",
        "text": "Please."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "请。"
    },
    {
        "voice": "narrator",
        "text": "Nice to meet you."
    },
    {
        "pause": 3000
    },
    {
        "voice": "male",
        "text": "很高兴认识你。"
    },
    {
        "voice": "narrator",
        "text": "Hello (formal version)."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "您好。"
    },
    {
        "voice": "narrator",
        "text": "Goodbye."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "再见。"
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 2 - SPEED ROUND)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Final accelerated round to establish effortless recall. Keep your energy up. Hello."
    },
    {
        "pause": 1500
    },
    {
        "voice": "female",
        "text": "你好。"
    },
    {
        "voice": "narrator",
        "text": "Correct."
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
        "text": "Incorrect."
    },
    {
        "pause": 1500
    },
    {
        "voice": "female",
        "text": "不对。"
    },
    {
        "voice": "narrator",
        "text": "I'm sorry."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "对不起。"
    },
    {
        "voice": "narrator",
        "text": "You're welcome."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "不客气。"
    },
    {
        "voice": "narrator",
        "text": "Good night."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "晚安。"
    },
    {
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

async def generate_tts(text, voice, output_file):
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate="-5%"
    )

    await communicate.save(output_file)

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