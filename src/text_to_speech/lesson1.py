import asyncio
import edge_tts
from pydub import AudioSegment

# =========================
# VOICE CONFIGURATION
# =========================

NARRATOR_VOICE = "en-US-AvaMultilingualNeural"
KOREAN_MALE = "ko-KR-InJoonNeural"
KOREAN_FEMALE = "ko-KR-SunHiNeural"

# =========================
# LESSON SCRIPT
# =========================

script = [
    # =========================================================
    # INTRODUCTION
    # =========================================================
    {
        "voice": "narrator",
        "text": "Welcome to Level 1, Topic 1 of your Korean Audio Coach. This course relies on your active participation. When you hear an English prompt followed by a pause, you must speak the Korean response out loud. Do not just listen silently. Let's begin."
    },
    {
        "voice": "narrator",
        "text": "Imagine you have just landed at Incheon International Airport in Seoul. You walk up to the immigration officer. To greet them politely, a native speaker says."
    },
    {
        "voice": "male",
        "text": "안녕하세요."
    },
    {
        "voice": "narrator",
        "text": "Listen again, and notice the soft ng sound at the end of the first two syllables. An-nyeong."
    },
    {
        "voice": "female",
        "text": "안녕하세요."
    },
    {
        "voice": "narrator",
        "text": "Now repeat out loud after the speaker. Match their pitch and melody."
    },
    {
        "voice": "male",
        "text": "안녕하세요."
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
        "text": "안녕하세요."
    },
    {
        "pause": 2000 
    },

    # =========================================================
    # MODULE 1: BASIC GREETINGS & TIME OF DAY
    # =========================================================
    {
        "voice": "narrator",
        "text": "Next up is the casual version of hello. Use this only with close friends, peers, or younger people. Hi."
    },
    {
        "voice": "male",
        "text": "안녕."
    },
    {
        "voice": "narrator",
        "text": "Listen to the female speaker. Notice how it is short and crisp."
    },
    {
        "voice": "female",
        "text": "안녕."
    },
    {
        "voice": "narrator",
        "text": "Your turn. Speak out loud. Hi."
    },
    {
        "voice": "male",
        "text": "안녕."
    },
    {
        "pause": 1500
    },
    {
        "voice": "narrator",
        "text": "Now, let's learn how to greet someone specifically in the morning. Good morning."
    },
    {
        "voice": "female",
        "text": "좋은 아침이에요."
    },
    {
        "voice": "narrator",
        "text": "Listen closely to the transitions between words. Good morning."
    },
    {
        "voice": "male",
        "text": "좋은 아침이에요."
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud after the speaker."
    },
    {
        "voice": "female",
        "text": "좋은 아침이에요."
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
        "text": "좋은 아침이에요."
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "Now, what if it is late at night? To wish someone well, we say: Good evening."
    },
    {
        "voice": "female",
        "text": "좋은 밤이에요."
    },
    {
        "voice": "narrator",
        "text": "Repeat after the male speaker. Good evening."
    },
    {
        "voice": "male",
        "text": "좋은 밤이에요."
    },
    {
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK A: GREETINGS REPETITION
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's test your memory on these first few phrases. I will give you the English, and you must say the Korean during the pause. Ready? Hello (polite)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "안녕하세요."
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
        "text": "안녕하세요."
    },
    {
        "voice": "narrator",
        "text": "How do you say 'Hi' casually to a friend?"
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "안녕."
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
        "text": "좋은 아침이에요."
    },
    {
        "voice": "narrator",
        "text": "And wish them a good evening."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "좋은 밤이에요."
    },

    # =========================================================
    # MODULE 2: GRATITUDE & POLITE PARTICLES
    # =========================================================
    {
        "voice": "narrator",
        "text": "Moving on to Module 2. Let's learn how to express gratitude. To thank someone formally, a native speaker says."
    },
    {
        "voice": "female",
        "text": "감사합니다."
    },
    {
        "voice": "narrator",
        "text": "Notice how the b sound in hap-ni-da softens into an m sound: gamsahamnida. Listen again."
    },
    {
        "voice": "male",
        "text": "감사합니다."
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Thank you."
    },
    {
        "voice": "female",
        "text": "감사합니다."
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "If you are talking to someone of similar status or slightly younger, you can use a casual polite form: Thanks."
    },
    {
        "voice": "male",
        "text": "고마워요."
    },
    {
        "voice": "narrator",
        "text": "Listen to the female speaker. Thanks."
    },
    {
        "voice": "female",
        "text": "고마워요."
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Thanks."
    },
    {
        "voice": "male",
        "text": "고마워요."
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "When someone thanks you, you should respond with 'You’re welcome'. Here is the traditional phrase."
    },
    {
        "voice": "female",
        "text": "천만에요."
    },
    {
        "voice": "narrator",
        "text": "Repeat after the male speaker. You're welcome."
    },
    {
        "voice": "male",
        "text": "천만에요."
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "Another common way to say 'No problem' or 'It's nothing' is: It's not / No."
    },
    {
        "voice": "female",
        "text": "아니에요."
    },
    {
        "voice": "narrator",
        "text": "Repeat. It's nothing."
    },
    {
        "voice": "male",
        "text": "아니에요."
    },
    {
        "pause": 2000
    },

    # =========================================================
    # RECALL BLOCK B: ALL PREVIOUS TOPICS (MODULE 1 + MODULE 2)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Time for our next cumulative recall loop. We will mix up greetings and gratitude. Do your best to answer quickly. How do you say Thank you formally?"
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "감사합니다."
    },
    {
        "voice": "narrator",
        "text": "How do you say Hello politely?"
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "안녕하세요."
    },
    {
        "voice": "narrator",
        "text": "How do you say Thanks in a casual polite way?"
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "고마워요."
    },
    {
        "voice": "narrator",
        "text": "Greet a close friend. Hi."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "안녕."
    },
    {
        "voice": "narrator",
        "text": "Respond to a thank you with 'You’re welcome'."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "천만에요."
    },
    {
        "voice": "narrator",
        "text": "Now say 'It’s nothing' or 'No problem'."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "아니에요."
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
        "text": "좋은 아침이에요."
    },

    # =========================================================
    # MODULE 3: AGREEMENT & DISAGREEMENT
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's master simple affirmation and negation in Module 3. To say a polite 'Yes', we say."
    },
    {
        "voice": "male",
        "text": "네."
    },
    {
        "voice": "narrator",
        "text": "Listen to the female speaker. It is short but clear. Yes."
    },
    {
        "voice": "female",
        "text": "네."
    },
    {
        "voice": "narrator",
        "text": "Repeat it now. Yes."
    },
    {
        "voice": "male",
        "text": "네."
    },
    {
        "pause": 1500
    },
    {
        "voice": "narrator",
        "text": "In highly formal or business settings, you might hear a different version of yes. Yes (formal)."
    },
    {
        "voice": "female",
        "text": "예."
    },
    {
        "voice": "narrator",
        "text": "Repeat the formal version. Yes."
    },
    {
        "voice": "male",
        "text": "예."
    },
    {
        "pause": 1500
    },
    {
        "voice": "narrator",
        "text": "Now let's learn how to say 'No'. No."
    },
    {
        "voice": "female",
        "text": "아니요."
    },
    {
        "voice": "narrator",
        "text": "Listen again. Notice the flat tone. No."
    },
    {
        "voice": "male",
        "text": "아니요."
    },
    {
        "voice": "narrator",
        "text": "Your turn to speak. No."
    },
    {
        "voice": "female",
        "text": "아니요."
    },
    {
        "pause": 2000
    },
    {
        "voice": "narrator",
        "text": "If someone asks if you are hurt or if something is wrong, you can tell them: It’s okay."
    },
    {
        "voice": "male",
        "text": "괜찮아요."
    },
    {
        "voice": "narrator",
        "text": "Listen carefully to the initial double-g sound. Gwaenchanayo."
    },
    {
        "voice": "female",
        "text": "괜찮아요."
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. It’s okay."
    },
    {
        "voice": "male",
        "text": "괜찮아요."
    },
    {
        "pause": 2500
    },

    # =========================================================
    # RECALL BLOCK C: ALL PREVIOUS TOPICS (MODULES 1, 2, + 3)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's perform a comprehensive review loop. Respond instantly in the pauses. Say: Yes (polite)."
    },
    {
        "pause": 1500
    },
    {
        "voice": "female",
        "text": "네."
    },
    {
        "voice": "narrator",
        "text": "Say: No."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "아니요."
    },
    {
        "voice": "narrator",
        "text": "Say: Thank you (formal)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "감사합니다."
    },
    {
        "voice": "narrator",
        "text": "Say: It's okay."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "괜찮아요."
    },
    {
        "voice": "narrator",
        "text": "Say: Yes (highly formal)."
    },
    {
        "pause": 1500
    },
    {
        "voice": "female",
        "text": "예."
    },
    {
        "voice": "narrator",
        "text": "Say: Hello."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "안녕하세요."
    },
    {
        "voice": "narrator",
        "text": "Say: Thanks (casual polite)."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "고마워요."
    },
    {
        "voice": "narrator",
        "text": "Say: Good evening."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "좋은 밤이에요."
    },

    # =========================================================
    # MODULE 4: NAVIGATION, APOLOGIES & APOLOGETIC PROTOCOLS
    # =========================================================
    {
        "voice": "narrator",
        "text": "In Module 4, let's look at how to get someone's attention or make your way through a crowded subway car. Excuse me."
    },
    {
        "voice": "female",
        "text": "실례합니다."
    },
    {
        "voice": "narrator",
        "text": "Listen closely to the hard 's' and soft 'l' transitions. Sillyehamnida."
    },
    {
        "voice": "male",
        "text": "실례합니다."
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Excuse me."
    },
    {
        "voice": "female",
        "text": "실례합니다."
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "Now, if you make a mistake, you must apologize. Here is the highly formal version: I'm sorry."
    },
    {
        "voice": "male",
        "text": "죄송합니다."
    },
    {
        "voice": "narrator",
        "text": "Listen to the female speaker. Use this with elders, bosses, or strangers. I'm sorry."
    },
    {
        "voice": "female",
        "text": "죄송합니다."
    },
    {
        "voice": "narrator",
        "text": "Repeat it clearly. I'm sorry."
    },
    {
        "voice": "male",
        "text": "죄송합니다."
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "If you are speaking to a peer or coworker in a softer setting, you can use the casual polite form: Sorry."
    },
    {
        "voice": "female",
        "text": "미안해요."
    },
    {
        "voice": "narrator",
        "text": "Listen again. Mianhaeyo."
    },
    {
        "voice": "male",
        "text": "미안해요."
    },
    {
        "voice": "narrator",
        "text": "Try speaking it out loud. Sorry."
    },
    {
        "voice": "female",
        "text": "미안해요."
    },
    {
        "pause": 2000
    },

    # =========================================================
    # RECALL BLOCK D: CUMULATIVE RECALL LOOP
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's test all your knowledge up to this point. I will quickly fire English prompts. Give me the Korean responses. Excuse me."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "실례합니다."
    },
    {
        "voice": "narrator",
        "text": "I'm sorry (formal)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "죄송합니다."
    },
    {
        "voice": "narrator",
        "text": "Sorry (casual polite)."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "미안해요."
    },
    {
        "voice": "narrator",
        "text": "It’s okay."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "괜찮아요."
    },
    {
        "voice": "narrator",
        "text": "Yes."
    },
    {
        "pause": 1500
    },
    {
        "voice": "male",
        "text": "네."
    },
    {
        "voice": "narrator",
        "text": "No."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "아니요."
    },
    {
        "voice": "narrator",
        "text": "Thank you."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "감사합니다."
    },
    {
        "voice": "narrator",
        "text": "Hi (casual)."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "안녕."
    },

    # =========================================================
    # MODULE 5: INTRODUCTIONS & BUSINESS ETIQUETTE
    # =========================================================
    {
        "voice": "narrator",
        "text": "Welcome to Module 5. When meeting someone for the first time in a formal or professional setting, you use a specific phrase. Nice to meet you."
    },
    {
        "voice": "male",
        "text": "처음 뵙겠습니다."
    },
    {
        "voice": "narrator",
        "text": "This literally translates to 'I am meeting you for the first time'. Listen to the female speaker."
    },
    {
        "voice": "female",
        "text": "처음 뵙겠습니다."
    },
    {
        "voice": "narrator",
        "text": "Try repeating this long phrase carefully. Nice to meet you."
    },
    {
        "voice": "male",
        "text": "처음 뵙겠습니다."
    },
    {
        "pause": 3000
    },
    {
        "voice": "narrator",
        "text": "There is another very common way to say nice to meet you, which means 'I am glad to see you'. Nice to meet you."
    },
    {
        "voice": "female",
        "text": "반갑습니다."
    },
    {
        "voice": "narrator",
        "text": "Listen to the male speaker. Bangapseumnida."
    },
    {
        "voice": "male",
        "text": "반갑습니다."
    },
    {
        "voice": "narrator",
        "text": "Your turn to speak. Nice to meet you."
    },
    {
        "voice": "female",
        "text": "반갑습니다."
    },
    {
        "pause": 2500
    },
    {
        "voice": "narrator",
        "text": "In Korean culture, when starting a new job, project, or relationship, you say a phrase that means 'Please look after me' or 'Please treat me well'. Please take care of me."
    },
    {
        "voice": "male",
        "text": "잘 부탁드립니다."
    },
    {
        "voice": "narrator",
        "text": "Listen carefully to the flow: Jal butakdeurimnida."
    },
    {
        "voice": "female",
        "text": "잘 부탁드립니다."
    },
    {
        "voice": "narrator",
        "text": "Repeat this vital business phrase out loud. Please take care of me."
    },
    {
        "voice": "male",
        "text": "잘 부탁드립니다."
    },
    {
        "pause": 3000
    },

    # =========================================================
    # RECALL BLOCK E: MEETING PEOPLE
    # =========================================================
    {
        "voice": "narrator",
        "text": "Let's practice the introduction mechanics. Speak the Korean translation during the pause. Nice to meet you (literal first time)."
    },
    {
        "pause": 3000
    },
    {
        "voice": "female",
        "text": "처음 뵙겠습니다."
    },
    {
        "voice": "narrator",
        "text": "Nice to meet you (I am glad)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "반갑습니다."
    },
    {
        "voice": "narrator",
        "text": "Please take care of me / Please look after me."
    },
    {
        "pause": 3000
    },
    {
        "voice": "female",
        "text": "잘 부탁드립니다."
    },

    # =========================================================
    # MODULE 6: THE ART OF SAYING GOODBYE
    # =========================================================
    {
        "voice": "narrator",
        "text": "In Module 6, we address a unique feature of the Korean language: parting ways. There are two distinct ways to say goodbye, depending on who is leaving and who is staying behind."
    },
    {
        "voice": "narrator",
        "text": "If you are staying put, and the other person is leaving, you tell them to 'go safely'. Goodbye to the person leaving."
    },
    {
        "voice": "male",
        "text": "안녕히 가세요."
    },
    {
        "voice": "narrator",
        "text": "Notice the verb 'ga-se-yo' which means please go. Listen again."
    },
    {
        "voice": "female",
        "text": "안녕히 가세요."
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Go safely."
    },
    {
        "voice": "male",
        "text": "안녕히 가세요."
    },
    {
        "pause": 3000
    },
    {
        "voice": "narrator",
        "text": "Now, if you are the one leaving, and the other person is staying behind, you tell them to 'stay safely'. Goodbye when you leave."
    },
    {
        "voice": "female",
        "text": "안녕히 계세요."
    },
    {
        "voice": "narrator",
        "text": "Notice the verb 'gye-se-yo' which means please stay. Listen again."
    },
    {
        "voice": "male",
        "text": "안녕히 계세요."
    },
    {
        "voice": "narrator",
        "text": "Repeat out loud. Stay safely."
    },
    {
        "voice": "female",
        "text": "안녕히 계세요."
    },
    {
        "pause": 3000
    },

    # =========================================================
    # RECALL BLOCK F: GOODBYES EXERCISE
    # =========================================================
    {
        "voice": "narrator",
        "text": "This distinction trips up many beginners. Let's practice intensely. Imagine you are leaving a coffee shop and the barista is staying. What do you say?"
    },
    {
        "pause": 3000
    },
    {
        "voice": "male",
        "text": "안녕히 계세요."
    },
    {
        "voice": "narrator",
        "text": "Now imagine you are hosting a friend at your apartment, and they are leaving to go home. What do you say?"
    },
    {
        "pause": 3000
    },
    {
        "voice": "female",
        "text": "안녕히 가세요."
    },
    {
        "voice": "narrator",
        "text": "Let's reverse it. You run out of an office building while your boss stays at their desk. Goodbye."
    },
    {
        "pause": 3000
    },
    {
        "voice": "male",
        "text": "안녕히 계세요."
    },
    {
        "voice": "narrator",
        "text": "Your guest walks out your front door. Goodbye."
    },
    {
        "pause": 3000
    },
    {
        "voice": "female",
        "text": "안녕히 가세요."
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 1)
    # =========================================================
    {
        "voice": "narrator",
        "text": "We have covered all twenty critical terms from your vocabulary index. To build bulletproof long-term retention, we will now dedicate the remaining minutes of this audio coaching session to an exhaustive, mixed-randomization challenge block. I will name an expression, and you must deploy it seamlessly. Let's go. Good morning."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "좋은 아침이에요."
    },
    {
        "voice": "narrator",
        "text": "Thank you (formal)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "감사합니다."
    },
    {
        "voice": "narrator",
        "text": "It’s not / No problem."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "아니에요."
    },
    {
        "voice": "narrator",
        "text": "Excuse me."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "실례합니다."
    },
    {
        "voice": "narrator",
        "text": "Nice to meet you (Glad to meet you variant)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "반갑습니다."
    },
    {
        "voice": "narrator",
        "text": "No."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "아니요."
    },
    {
        "voice": "narrator",
        "text": "Goodbye (to a person who is leaving your sight)."
    },
    {
        "pause": 3000
    },
    {
        "voice": "male",
        "text": "안녕히 가세요."
    },
    {
        "voice": "narrator",
        "text": "Thanks (casual polite)."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "고마워요."
    },
    {
        "voice": "narrator",
        "text": "I’m sorry (formal protocol)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "죄송합니다."
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 2)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Continuing our deep-recall sequence. Keep up the momentum. Speak clearly. Nice to meet you (formal/first time format)."
    },
    {
        "pause": 3000
    },
    {
        "voice": "female",
        "text": "처음 뵙겠습니다."
    },
    {
        "voice": "narrator",
        "text": "Yes (highly formal variant)."
    },
    {
        "pause": 1500
    },
    {
        "voice": "male",
        "text": "예."
    },
    {
        "voice": "narrator",
        "text": "It’s okay."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "괜찮아요."
    },
    {
        "voice": "narrator",
        "text": "Please take care of me / Look after this relationship well."
    },
    {
        "pause": 3000
    },
    {
        "voice": "male",
        "text": "잘 부탁드립니다."
    },
    {
        "voice": "narrator",
        "text": "Goodbye (when you are departing and they are staying)."
    },
    {
        "pause": 3000
    },
    {
        "voice": "female",
        "text": "안녕히 계세요."
    },
    {
        "voice": "narrator",
        "text": "You’re welcome."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "천만에요."
    },
    {
        "voice": "narrator",
        "text": "Sorry (casual polite version)."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "미안해요."
    },
    {
        "voice": "narrator",
        "text": "Good evening."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "좋은 밤이에요."
    },
    {
        "voice": "narrator",
        "text": "Hello (polite everyday version)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "안녕하세요."
    },

    # =========================================================
    # FINAL COMPREHENSIVE RECALL ARCH (BLOCK 3 - ULTRA ACCELERATED)
    # =========================================================
    {
        "voice": "narrator",
        "text": "Final lightning round. No hints. Say the Korean phrases immediately. Yes."
    },
    {
        "pause": 1500
    },
    {
        "voice": "male",
        "text": "네."
    },
    {
        "voice": "narrator",
        "text": "No."
    },
    {
        "pause": 1500
    },
    {
        "voice": "female",
        "text": "아니요."
    },
    {
        "voice": "narrator",
        "text": "Hi (casual)."
    },
    {
        "pause": 1500
    },
    {
        "voice": "male",
        "text": "안녕."
    },
    {
        "voice": "narrator",
        "text": "Thank you."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "감사합니다."
    },
    {
        "voice": "narrator",
        "text": "Excuse me."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "실례합니다."
    },
    {
        "voice": "narrator",
        "text": "I'm sorry."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "죄송합니다."
    },
    {
        "voice": "narrator",
        "text": "It’s okay."
    },
    {
        "pause": 2000
    },
    {
        "voice": "male",
        "text": "괜찮아요."
    },
    {
        "voice": "narrator",
        "text": "Nice to meet you (Glad version)."
    },
    {
        "pause": 2000
    },
    {
        "voice": "female",
        "text": "반갑습니다."
    },
    {
        "voice": "narrator",
        "text": "Goodbye (other person leaves)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "male",
        "text": "안녕히 가세요."
    },
    {
        "voice": "narrator",
        "text": "Goodbye (you leave)."
    },
    {
        "pause": 2500
    },
    {
        "voice": "female",
        "text": "안녕히 계세요."
    },
    {
        "voice": "narrator",
        "text": "Excellent work. You have systematically moved through all foundational conversational building blocks. Consistent verbal production ensures long term retention. Class dismissed."
    }
]

# =========================
# VOICE SELECTOR
# =========================

def get_voice(voice_type):
    if voice_type == "narrator":
        return NARRATOR_VOICE
    elif voice_type == "male":
        return KOREAN_MALE
    elif voice_type == "female":
        return KOREAN_FEMALE
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