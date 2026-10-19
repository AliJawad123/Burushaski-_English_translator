
import streamlit as st
import streamlit.components.v1 as components
import random

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Six Months of Us ❤️",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# PERSONALIZE YOUR WEBSITE HERE
# --------------------------------------------------
YOUR_NAME = "Your Name"
HER_NAME = "My Beautiful Girl"
ANNIVERSARY_DATE = "Our Special Day"
YEARS_OR_MONTHS = "Six Months"

LOVE_LETTER = """
My love,

Happy six-month anniversary to us. ❤️

These six months have given me so many reasons to
smile, so many beautiful memories, and one more
reason every day to look forward to our future.

You are more than the person I love. You are the
person I want to share my ordinary days, my biggest
dreams, my happiest moments, and even my difficult
days with.

I may not always find the perfect words to explain
what you mean to me, but I hope I can spend a
lifetime showing you.

Today is six months of us, and I pray that one day
we will look back at this little website together
and smile at how our forever began.

Thank you for being you.

Six months down, a lifetime to go.

Forever yours. ❤️
"""

REASONS = [
    ("♡", "Your Kind Heart",
     "You care deeply, and the kindness in you makes my world better."),
    ("✧", "Your Smile",
     "Your smile can make an ordinary day feel extraordinary."),
    ("❀", "Your Strength",
     "I admire the way you face challenges with courage and grace."),
    ("☾", "Your Beautiful Mind",
     "I love your thoughts, your perspective, and the person you are."),
    ("∞", "The Little Things",
     "The little moments with you become the memories I treasure."),
    ("♥", "Simply You",
     "I don't need a reason to love you. Being you is more than enough."),
]

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "letter_open" not in st.session_state:
    st.session_state.letter_open = False

if "final_reveal" not in st.session_state:
    st.session_state.final_reveal = False

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;500;600;700&family=Poppins:wght@300;400;500;600&display=swap');

:root {
    --pink: #ff8eaa;
    --light-pink: #ffd1df;
    --deep-pink: #d94f7b;
    --cream: #fff1f5;
    --dark: #100d16;
    --card: rgba(255, 225, 238, 0.055);
}

html {
    scroll-behavior: smooth;
}

.stApp {
    background:
        radial-gradient(ellipse at 15% 15%,
            rgba(143, 39, 82, 0.18), transparent 42%),
        radial-gradient(ellipse at 85% 40%,
            rgba(91, 38, 102, 0.16), transparent 40%),
        linear-gradient(145deg, #100d16, #1b101b 55%, #100d16);
    color: var(--cream);
    font-family: 'Poppins', sans-serif;
}

header[data-testid="stHeader"] {
    background: rgba(16, 13, 22, 0.8);
}

footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    max-width: 1150px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

h1, h2, h3, p {
    color: var(--cream);
}

.hero {
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: 65px 22px 55px;
    border: 1px solid rgba(255, 142, 170, 0.18);
    border-radius: 28px;
    background:
        radial-gradient(circle at 50% 30%,
            rgba(177, 60, 108, 0.24), transparent 60%),
        linear-gradient(135deg,
            rgba(255,255,255,0.035),
            rgba(255,142,170,0.025));
    box-shadow: 0 18px 70px rgba(0,0,0,0.2);
    animation: fadeUp 1.2s ease both;
}

.eyebrow {
    color: var(--pink);
    font-size: 0.8rem;
    font-weight: 500;
    letter-spacing: 4px;
    text-transform: uppercase;
}

.script {
    font-family: 'Great Vibes', cursive;
    color: var(--light-pink);
    font-weight: 400;
}

.hero h1 {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(3.5rem, 8vw, 6.8rem);
    line-height: 1.12;
    font-weight: 400;
    margin: 20px 0 12px;
    text-shadow: 0 0 35px rgba(255,142,170,0.2);
}

.hero .subtitle {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.05rem, 2.5vw, 1.5rem);
    color: #f7c5d5;
}

.hero .intro {
    max-width: 620px;
    margin: 20px auto;
    line-height: 1.9;
    color: #eadbe3;
}

.glow-heart {
    display: inline-block;
    color: var(--pink);
    font-size: 2rem;
    animation: heartbeat 1.6s infinite;
    text-shadow: 0 0 22px rgba(255,80,140,0.8);
}

.section-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.8rem, 4vw, 2.5rem);
    color: var(--light-pink);
    margin-top: 55px;
    margin-bottom: 8px;
}

.section-subtitle {
    text-align: center;
    color: #cdb8c5;
    margin-bottom: 28px;
}

.love-card {
    height: 205px;
    padding: 24px 18px;
    border: 1px solid rgba(255,142,170,0.4);
    border-radius: 18px;
    background: var(--card);
    text-align: center;
    margin-bottom: 16px;
    transition: transform .3s ease, background .3s ease,
                box-shadow .3s ease;
    animation: fadeUp .8s ease both;
}

.love-card:hover {
    transform: translateY(-7px);
    background: rgba(255,142,170,0.10);
    box-shadow: 0 12px 35px rgba(255,90,140,0.10);
}

.card-icon {
    font-size: 2rem;
    color: var(--pink);
    margin-bottom: 8px;
}

.card-title {
    font-family: 'Playfair Display', serif;
    color: #ffe1ea;
    font-size: 1.12rem;
    margin-bottom: 10px;
    font-weight: 600;
}

.card-text {
    font-size: .88rem;
    color: #dfcbd6;
    line-height: 1.65;
}

.memory-card {
    border-left: 2px solid var(--pink);
    padding: 4px 0 8px 22px;
    margin: 22px 0;
    position: relative;
}

.memory-card:before {
    content: '♥';
    position: absolute;
    left: -12px;
    top: 0;
    background: #1b101b;
    color: var(--pink);
    padding: 0 3px;
}

.memory-date {
    color: var(--pink);
    font-size: .78rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.memory-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    color: #ffe1ea;
    margin: 6px 0;
}

.memory-text {
    color: #d9c5d1;
    line-height: 1.7;
}

.letter {
    background: linear-gradient(145deg,
        rgba(255, 218, 231, .09),
        rgba(255, 255, 255, .025));
    border: 1px solid rgba(255,142,170,.45);
    border-radius: 20px;
    padding: clamp(22px, 5vw, 42px);
    line-height: 2;
    color: #f8dce7;
    white-space: pre-wrap;
    box-shadow: 0 10px 45px rgba(0,0,0,.16);
    animation: fadeUp .8s ease both;
}

.promise {
    text-align: center;
    padding: 35px 20px;
    border-radius: 22px;
    border: 1px solid rgba(255,142,170,.2);
    background: rgba(255,142,170,.035);
}

.promise h2 {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(2.6rem, 6vw, 4.5rem);
    font-weight: 400;
    color: var(--light-pink);
}

.promise p {
    color: #e2c9d5;
    line-height: 1.8;
}

.stButton > button {
    border-radius: 100px;
    border: 1px solid rgba(255,142,170,.65);
    background: linear-gradient(100deg, #ff9fba, #ffd1df);
    color: #381522;
    padding: 0.72rem 1.6rem;
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    transition: all .25s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    border-color: #fff0f5;
    box-shadow: 0 6px 25px rgba(255,100,150,.25);
    color: #381522;
}

div[data-testid="stHorizontalBlock"] {
    gap: 1rem;
}

.footer {
    text-align: center;
    padding: 35px 10px 10px;
    color: #a991a0;
    font-size: .85rem;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    15% { transform: scale(1.18); }
    30% { transform: scale(1); }
    45% { transform: scale(1.12); }
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(22px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Floating hearts are decorative and ignore mouse clicks */
.floating-heart {
    position: fixed;
    bottom: -45px;
    z-index: 0;
    color: rgba(255, 130, 165, .5);
    pointer-events: none;
    animation: floatHeart linear infinite;
}

@keyframes floatHeart {
    0% { transform: translateY(0) rotate(0deg); opacity: 0; }
    15% { opacity: .8; }
    85% { opacity: .6; }
    100% { transform: translateY(-110vh) rotate(35deg); opacity: 0; }
}

@media (max-width: 650px) {
    .hero { padding: 42px 14px; }
    .eyebrow { letter-spacing: 2px; font-size: .68rem; }
    .love-card { height: auto; min-height: 175px; }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# FLOATING HEARTS
# --------------------------------------------------
components.html("""
<div id="heart-layer"></div>
<style>
#heart-layer {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 999;
    overflow: hidden;
}
.float-heart {
    position: absolute;
    bottom: -40px;
    color: #ff85aa;
    opacity: 0;
    animation: drift linear infinite;
    filter: drop-shadow(0 0 7px rgba(255,90,150,.35));
}
@keyframes drift {
    0% { transform: translateY(0) rotate(0deg); opacity: 0; }
    15% { opacity: .6; }
    85% { opacity: .5; }
    100% { transform: translateY(-110vh) rotate(40deg); opacity: 0; }
}
</style>
<script>
const layer = document.getElementById("heart-layer");
const symbols = ["♡", "♥", "✧", "❤"];

for (let i = 0; i < 24; i++) {
    const heart = document.createElement("span");
    heart.className = "float-heart";
    heart.textContent = symbols[Math.floor(Math.random() * symbols.length)];
    heart.style.left = Math.random() * 100 + "%";
    heart.style.animationDuration = (9 + Math.random() * 13) + "s";
    heart.style.animationDelay = (Math.random() * 15) + "s";
    heart.style.fontSize = (14 + Math.random() * 22) + "px";
    layer.appendChild(heart);
}
</script>
""", height=0)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown(f"""
<div class="hero">
    <div class="eyebrow">♥ &nbsp; HAPPY HALF-YEAR ANNIVERSARY &nbsp; ♥</div>
    <h1>Six Months...<br>and a lifetime to go</h1>
    <div class="glow-heart">♡</div>
    <div class="subtitle">To {HER_NAME}, my favourite person</div>
    <p class="intro">
        Thank you for being a part of my story.<br>
        You make my world brighter, calmer and so much more beautiful.<br>
        Here's a little piece of my heart, made just for you.
    </p>
    <p style="color:#ffb4ca; letter-spacing:2px;">
        {ANNIVERSARY_DATE}
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div style="height:12px"></div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# SIX REASONS
# --------------------------------------------------
st.markdown("""
<div class="section-title">Six Reasons I Love You</div>
<div class="section-subtitle">
    Six reasons, but a lifetime of love.
</div>
""", unsafe_allow_html=True)

for start in range(0, len(REASONS), 3):
    cols = st.columns(3)
    for col, reason in zip(cols, REASONS[start:start + 3]):
        icon, title, description = reason
        with col:
            st.markdown(f"""
            <div class="love-card">
                <div class="card-icon">{icon}</div>
                <div class="card-title">{title}</div>
                <div class="card-text">{description}</div>
            </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------
# OUR JOURNEY
# EDIT THESE TO MATCH YOUR REAL STORY
# --------------------------------------------------
st.markdown("""
<div class="section-title">Our Journey</div>
<div class="section-subtitle">
    From the first moments to the future we dream about.
</div>
""", unsafe_allow_html=True)

journey = [
    ("THE BEGINNING", "When Our Story Began",
     "A new chapter started, and someone special began to mean more to me."),
    ("GETTING CLOSER", "Little Moments, Big Feelings",
     "Conversations, smiles and memories that made our connection stronger."),
    ("SIX MONTHS", "Half a Year of Us",
     "Six months of learning, caring and choosing to build something beautiful."),
    ("OUR FUTURE", "A Lifetime Together",
     "The next chapter is the one I look forward to most: our life together."),
]

for date, title, description in journey:
    st.markdown(f"""
    <div class="memory-card">
        <div class="memory-date">{date}</div>
        <div class="memory-title">{title}</div>
        <div class="memory-text">{description}</div>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# LOVE LETTER
# --------------------------------------------------
st.markdown("""
<div class="section-title">A Letter From My Heart</div>
<div class="section-subtitle">
    Some things are too special to leave unsaid.
</div>
""", unsafe_allow_html=True)

left, center, right = st.columns([1, 2, 1])
with center:
    if not st.session_state.letter_open:
        if st.button("💌  Open Your Love Letter", use_container_width=True):
            st.session_state.letter_open = True
            st.rerun()
    else:
        st.markdown(
            f'<div class="letter">{LOVE_LETTER}</div>',
            unsafe_allow_html=True
        )
        if st.button("♡ Close the letter", use_container_width=True):
            st.session_state.letter_open = False
            st.rerun()

# --------------------------------------------------
# FINAL SURPRISE
# --------------------------------------------------
st.markdown("""
<div class="section-title">One Last Little Surprise</div>
<div class="section-subtitle">
    There's something I want you to remember.
</div>
""", unsafe_allow_html=True)

left, center, right = st.columns([1, 2, 1])
with center:
    if st.button("❤️ Click for a little promise", use_container_width=True):
        st.session_state.final_reveal = not st.session_state.final_reveal

if st.session_state.final_reveal:
    st.balloons()
    st.markdown(f"""
    <div class="promise">
        <div class="glow-heart">♥</div>
        <h2>My Promise to You</h2>
        <p>
            I cannot promise that every day will be perfect.<br>
            But I promise to keep learning, keep caring,<br>
            keep choosing us, and keep making room for your happiness.<br><br>
            I hope this is only the beginning of our favourite story.
        </p>
        <h2>Six Months Down.<br>A Lifetime to Go.</h2>
        <p>Forever yours,<br><strong>{YOUR_NAME}</strong></p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(f"""
<div class="footer">
    Made with ♡, especially for {HER_NAME}<br>
    <span style="color:#ff8eaa">
        Every love story is special. Ours is my favourite.
    </span>
</div>
""", unsafe_allow_html=True)
