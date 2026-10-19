
import streamlit as st
import streamlit.components.v1 as components
import html

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Six Months of Us ❤️",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# 2. PERSONALIZE YOUR WEBSITE
# =========================================================
YOUR_NAME = "Jawad"
HER_NAME = "My Daltas Jasmine"
ANNIVERSARY_DATE = "19 October 2026"

# Replace these sample messages with your own memories.
LOVE_LETTER = """
My love,

Happy six-month anniversary to us. ❤️

These six months have given me so many reasons to smile,
so many beautiful memories, and one more reason every day
to look forward to our future.

You are the person I want to share my ordinary days,
my biggest dreams, my happiest moments, and even my
difficult days with.

I may not always find the perfect words to explain what
you mean to me, but I hope I can spend a lifetime
showing you.

Today is six months of us, and I pray that one day we
will look back at this little website together and smile
at how our forever began.

Thank you for being you.

Six months down, a lifetime to go.

Forever yours. ❤️
"""

REASONS = [
    (
        "♡",
        "Your Kind Heart",
        "You care deeply, and your kindness makes my world better."
    ),
    (
        "✧",
        "Your Smile",
        "Your smile can make an ordinary day feel extraordinary."
    ),
    (
        "❀",
        "Your Strength",
        "I admire the way you face challenges with courage and grace."
    ),
    (
        "☾",
        "Your Beautiful Mind",
        "I love your thoughts, your perspective, and who you are."
    ),
    (
        "🌸",
        "The Little Things",
        "The little moments with you become memories I treasure."
    ),
    (
        "∞",
        "Simply You",
        "I don't need a reason to love you. Being you is enough."
    ),
]

JOURNEY = [
    (
        "THE BEGINNING",
        "When Our Story Began",
        "A new chapter started, and someone special began to mean more to me."
    ),
    (
        "GETTING CLOSER",
        "Little Moments, Big Feelings",
        "Conversations, smiles, and memories made our connection stronger."
    ),
    (
        "SIX MONTHS",
        "Half a Year of Us",
        "Six months of learning, caring, and building something beautiful."
    ),
    (
        "OUR FUTURE",
        "A Lifetime Together",
        "The next chapter is the one I look forward to most: our life together."
    ),
]

# =========================================================
# 3. SESSION STATE
# =========================================================
if "started" not in st.session_state:
    st.session_state.started = False

if "letter_open" not in st.session_state:
    st.session_state.letter_open = False

if "final_reveal" not in st.session_state:
    st.session_state.final_reveal = False

# =========================================================
# 4. GLOBAL STYLING
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;500;600;700&family=Poppins:wght@300;400;500;600&display=swap');

:root {
    --gold: #f3d99b;
    --pink: #f6b9c8;
    --cream: #fff2d9;
    --text: #eee8d9;
    --muted: #d0cdbd;
    --dark: #192522;
}

html {
    scroll-behavior: smooth;
}

.stApp {
    color: var(--text);
    background:
        radial-gradient(ellipse at 10% 8%,
            rgba(112, 155, 119, .22), transparent 40%),
        radial-gradient(ellipse at 90% 30%,
            rgba(192, 142, 122, .14), transparent 38%),
        linear-gradient(145deg, #18221f, #26332c 52%, #191f23);
    font-family: 'Poppins', sans-serif;
}

header[data-testid="stHeader"] {
    background: rgba(25, 37, 34, .78);
}

footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    max-width: 1120px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p {
    color: var(--cream);
}

hr {
    border-color: rgba(243, 217, 155, .18);
}

/* ---------------- WELCOME SCREEN ---------------- */

.welcome-screen {
    position: relative;
    overflow: hidden;
    min-height: 490px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 48px 22px;
    border-radius: 30px;
    border: 1px solid rgba(255, 238, 191, .35);
    background:
        radial-gradient(ellipse at 50% 12%,
            rgba(255, 231, 173, .26), transparent 40%),
        radial-gradient(ellipse at 15% 85%,
            rgba(118, 165, 125, .25), transparent 45%),
        linear-gradient(180deg,
            #526e68 0%,
            #344e48 45%,
            #202e2b 100%);
    box-shadow:
        inset 0 0 70px rgba(255, 232, 174, .08),
        0 18px 55px rgba(0, 0, 0, .22);
    animation: fadeUp 1.2s ease both;
}

.welcome-screen::before,
.welcome-screen::after {
    content: "✦  ·  ✧  ·  ✦";
    position: absolute;
    color: rgba(255, 233, 181, .65);
    font-size: 22px;
    letter-spacing: 20px;
    animation: twinkle 3s ease-in-out infinite alternate;
    pointer-events: none;
}

.welcome-screen::before {
    top: 35px;
    left: 8%;
}

.welcome-screen::after {
    bottom: 35px;
    right: 5%;
    animation-delay: 1.2s;
}

.welcome-kicker {
    color: #ffe6ae;
    font-size: .77rem;
    font-weight: 500;
    letter-spacing: 4px;
    text-transform: uppercase;
}

.welcome-title {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(3.8rem, 9vw, 6.7rem);
    line-height: 1.12;
    font-weight: 400;
    color: #fff0ca;
    text-shadow: 0 0 30px rgba(255, 229, 165, .28);
    margin: 20px 0;
}

.welcome-text {
    max-width: 590px;
    color: #f4eddb;
    font-size: 1rem;
    line-height: 1.9;
}

.welcome-decor {
    font-size: 2.4rem;
    margin-bottom: 20px;
    animation: float 4s ease-in-out infinite;
}

.welcome-hint {
    color: #f5dfb5;
    font-size: .82rem;
    margin-top: 10px;
    letter-spacing: 1px;
}

div[data-testid="stButton"] > button {
    border-radius: 100px;
    border: 1px solid rgba(255, 245, 213, .7);
    background: linear-gradient(110deg, #f4d9a1, #f3bdc2);
    color: #374239;
    padding: .72rem 1.3rem;
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    transition: all .25s ease;
}

div[data-testid="stButton"] > button:hover {
    transform: translateY(-3px);
    border-color: #fff5df;
    color: #26332c;
    box-shadow: 0 8px 28px rgba(255, 218, 157, .25);
}

/* ---------------- HERO ---------------- */

.hero {
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: 48px 20px;
    border-radius: 26px;
    border: 1px solid rgba(243, 217, 155, .22);
    background:
        radial-gradient(ellipse at 50% 25%,
            rgba(222, 175, 133, .14), transparent 60%),
        rgba(255, 255, 255, .025);
    box-shadow: 0 15px 55px rgba(0, 0, 0, .15);
    animation: fadeUp 1s ease both;
}

.eyebrow {
    color: var(--gold);
    font-size: .77rem;
    letter-spacing: 3px;
    font-weight: 500;
}

.script {
    font-family: 'Great Vibes', cursive;
    color: var(--pink);
}

.hero h1 {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(3.5rem, 8vw, 6.4rem);
    line-height: 1.12;
    font-weight: 400;
    color: #fff0d6;
    margin: 22px 0 12px;
}

.hero .subtitle {
    font-family: 'Playfair Display', serif;
    color: var(--gold);
    font-size: clamp(1.05rem, 2.5vw, 1.45rem);
}

.intro {
    max-width: 650px;
    margin: 20px auto;
    line-height: 1.9;
    color: #e9e5d8;
}

.glow-heart {
    display: inline-block;
    color: var(--pink);
    font-size: 2rem;
    animation: heartbeat 1.8s infinite;
    text-shadow: 0 0 22px rgba(255, 180, 200, .65);
}

/* ---------------- SECTIONS ---------------- */

.section-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.8rem, 4vw, 2.5rem);
    color: var(--gold);
    margin-top: 52px;
    margin-bottom: 8px;
}

.section-subtitle {
    text-align: center;
    color: var(--muted);
    margin-bottom: 28px;
    line-height: 1.7;
}

/* ---------------- LOVE CARDS ---------------- */

.love-card {
    min-height: 215px;
    height: 100%;
    box-sizing: border-box;
    padding: 24px 16px;
    border: 1px solid rgba(243, 217, 155, .35);
    border-radius: 20px;
    background: rgba(235, 231, 205, .055);
    text-align: center;
    margin-bottom: 16px;
    transition: transform .3s ease, background .3s ease,
                box-shadow .3s ease;
    animation: fadeUp .8s ease both;
}

.love-card:hover {
    transform: translateY(-7px);
    background: rgba(243, 217, 155, .09);
    box-shadow: 0 12px 32px rgba(0, 0, 0, .15);
}

.card-icon {
    font-size: 2rem;
    color: var(--gold);
    margin-bottom: 10px;
}

.card-title {
    font-family: 'Playfair Display', serif;
    color: #fff0d6;
    font-size: 1.12rem;
    margin-bottom: 10px;
    font-weight: 600;
}

.card-text {
    font-size: .86rem;
    color: #dcdccd;
    line-height: 1.7;
}

/* ---------------- TIMELINE ---------------- */

.memory-card {
    position: relative;
    border-left: 2px solid #d8c18d;
    padding: 4px 0 12px 23px;
    margin: 22px 0;
}

.memory-card::before {
    content: "♥";
    position: absolute;
    left: -12px;
    top: 0;
    padding: 0 3px;
    color: #f5c3c9;
    background: #24312c;
}

.memory-date {
    color: var(--gold);
    font-size: .76rem;
    letter-spacing: 2px;
}

.memory-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    color: #fff0d6;
    margin: 6px 0;
}

.memory-text {
    color: #dcdccd;
    line-height: 1.8;
}

/* ---------------- LOVE LETTER ---------------- */

.letter {
    background: linear-gradient(145deg,
        rgba(243, 217, 155, .09),
        rgba(255, 255, 255, .025));
    border: 1px solid rgba(243, 217, 155, .42);
    border-radius: 22px;
    padding: clamp(22px, 5vw, 42px);
    line-height: 2;
    color: #f6e7d1;
    white-space: pre-wrap;
    box-shadow: 0 12px 40px rgba(0, 0, 0, .16);
    animation: fadeUp .8s ease both;
}

/* ---------------- FINAL PROMISE ---------------- */

.promise {
    text-align: center;
    padding: 35px 20px;
    border-radius: 24px;
    border: 1px solid rgba(243, 217, 155, .3);
    background: rgba(243, 217, 155, .045);
}

.promise h2 {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(2.8rem, 6vw, 4.5rem);
    font-weight: 400;
    color: #fff0ca;
}

.promise p {
    color: #e9e2d3;
    line-height: 1.9;
}

/* ---------------- FOOTER ---------------- */

.footer {
    text-align: center;
    padding: 36px 10px 10px;
    color: #b8b8a7;
    font-size: .84rem;
    line-height: 2;
}

/* ---------------- ANIMATIONS ---------------- */

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    15% { transform: scale(1.17); }
    30% { transform: scale(1); }
    45% { transform: scale(1.1); }
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

@keyframes twinkle {
    from { opacity: .35; transform: translateY(0); }
    to { opacity: 1; transform: translateY(-5px); }
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 650px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .welcome-screen {
        min-height: 420px;
        padding: 35px 15px;
    }

    .welcome-kicker {
        letter-spacing: 2px;
        font-size: .68rem;
    }

    .love-card {
        min-height: 190px;
        padding: 20px 12px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 5. FLOATING HEARTS AND SPARKLES
# =========================================================
# Separate iframe so the decorative animation does not
# interfere with Streamlit buttons or other interactions.
components.html("""
<div id="magic-sky"></div>

<style>
html, body {
    margin: 0;
    background: transparent;
    overflow: hidden;
}

#magic-sky {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
}

.magic-particle {
    position: absolute;
    bottom: -40px;
    animation: floatUp linear infinite;
    opacity: 0;
    color: #f5d5a0;
    text-shadow: 0 0 8px rgba(245, 213, 160, .4);
}

@keyframes floatUp {
    0% {
        transform: translateY(0) rotate(0);
        opacity: 0;
    }
    15% { opacity: .65; }
    80% { opacity: .5; }
    100% {
        transform: translateY(-105vh) rotate(40deg);
        opacity: 0;
    }
}
</style>

<script>
const sky = document.getElementById("magic-sky");
const symbols = ["♡", "✦", "✧", "♥", "❀"];

for (let i = 0; i < 22; i++) {
    const particle = document.createElement("span");
    particle.className = "magic-particle";
    particle.textContent =
        symbols[Math.floor(Math.random() * symbols.length)];

    particle.style.left = Math.random() * 100 + "%";
    particle.style.animationDuration =
        (10 + Math.random() * 12) + "s";
    particle.style.animationDelay =
        (Math.random() * 15) + "s";
    particle.style.fontSize =
        (13 + Math.random() * 18) + "px";

    sky.appendChild(particle);
}
</script>
""", height=1)

# =========================================================
# 6. MAGICAL OPENING SCREEN
# =========================================================
if not st.session_state.started:

    st.markdown("""
    <div class="welcome-screen">
        <div class="welcome-decor">🌿 ✨ 🌙</div>

        <div class="welcome-kicker">
            A LITTLE WORLD MADE JUST FOR YOU
        </div>

        <div class="welcome-title">
            Once Upon<br>a Time...
        </div>

        <div class="welcome-text">
            Somewhere between two hearts, a beautiful
            story began.<br>
            Today, that story is celebrating six magical
            months.<br><br>
            I have a little surprise for you, my love.
        </div>

        <div class="welcome-decor" style="margin-top:24px;">
            🦋 ♡ 🦋
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>",
                unsafe_allow_html=True)

    _, center, _ = st.columns([1, 1, 1])

    with center:
        st.markdown("""
        <div style="text-align:center; margin-bottom:8px;
                    color:#ffe6ae; font-size:.85rem;">
            ✨ A little magic is waiting ✨
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "✧   A   ✧",
            key="magic_a",
            use_container_width=True,
        ):
            st.session_state.started = True
            st.balloons()
            st.rerun()

        st.markdown("""
        <div class="welcome-hint" style="text-align:center">
            Touch the magic to open your surprise
        </div>
        """, unsafe_allow_html=True)

    # Hide the rest of the page until she clicks A.
    st.stop()

# =========================================================
# 7. CONGRATULATIONS REVEAL
# =========================================================
st.markdown(f"""
<div class="welcome-screen"
     style="min-height:0; padding:36px 20px;">

    <div class="welcome-decor">🌸 ✨ 💗 ✨ 🌸</div>

    <div class="welcome-kicker">
        A SPECIAL CELEBRATION FOR US
    </div>

    <div class="welcome-title" style="font-size:4.2rem;">
        Happy Six Months!
    </div>

    <div class="welcome-text">
        Congratulations to us, my love!<br>
        Six months of our story, and so many beautiful
        chapters still waiting to be written.<br><br>

        <span style="color:#ffe6ae; font-size:1.15rem;">
            You are my favourite kind of magic. ♡
        </span>
    </div>

    <div style="color:#ffe6ae; margin-top:20px;">
        {html.escape(ANNIVERSARY_DATE)}
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 8. MAIN ANNIVERSARY HERO
# =========================================================
st.markdown(f"""
<div class="hero">
    <div class="eyebrow">
        ♥ &nbsp; HAPPY HALF-YEAR ANNIVERSARY &nbsp; ♥
    </div>

    <h1>Six Months...<br>and a lifetime to go</h1>

    <div class="glow-heart">♡</div>

    <div class="subtitle">
        To {html.escape(HER_NAME)}, my favourite person
    </div>

    <p class="intro">
        Thank you for being a part of my story.<br>
        You make my world brighter, calmer and so much
        more beautiful.<br>
        Here's a little piece of my heart, made just for you.
    </p>

    <p style="color:#f3d99b; letter-spacing:2px;">
        {html.escape(ANNIVERSARY_DATE)}
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 9. SIX REASONS I LOVE YOU
# =========================================================
st.markdown("""
<div class="section-title">Six Reasons I Love You</div>
<div class="section-subtitle">
    Six reasons, but a lifetime of love.
</div>
""", unsafe_allow_html=True)

for start in range(0, len(REASONS), 3):
    columns = st.columns(3)

    for column, reason in zip(
        columns, REASONS[start:start + 3]
    ):
        icon, title, description = reason

        with column:
            st.markdown(f"""
            <div class="love-card">
                <div class="card-icon">{icon}</div>
                <div class="card-title">
                    {html.escape(title)}
                </div>
                <div class="card-text">
                    {html.escape(description)}
                </div>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# 10. OUR JOURNEY
# =========================================================
st.markdown("""
<div class="section-title">Our Journey</div>
<div class="section-subtitle">
    From the first moments to the future we dream about.
</div>
""", unsafe_allow_html=True)

for date, title, description in JOURNEY:
    st.markdown(f"""
    <div class="memory-card">
        <div class="memory-date">
            {html.escape(date)}
        </div>
        <div class="memory-title">
            {html.escape(title)}
        </div>
        <div class="memory-text">
            {html.escape(description)}
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 11. INTERACTIVE LOVE LETTER
# =========================================================
st.markdown("""
<div class="section-title">A Letter From My Heart</div>
<div class="section-subtitle">
    Some things are too special to leave unsaid.
</div>
""", unsafe_allow_html=True)

_, letter_col, _ = st.columns([1, 2, 1])

with letter_col:
    if not st.session_state.letter_open:
        if st.button(
            "💌 Open Your Love Letter",
            use_container_width=True,
        ):
            st.session_state.letter_open = True
            st.rerun()
    else:
        # Escape user-provided text so it displays as text,
        # rather than being interpreted as HTML.
        safe_letter = html.escape(LOVE_LETTER)

        st.markdown(
            f'<div class="letter">{safe_letter}</div>',
            unsafe_allow_html=True,
        )

        if st.button(
            "♡ Close the letter",
            use_container_width=True,
        ):
            st.session_state.letter_open = False
            st.rerun()

# =========================================================
# 12. THE FINAL SURPRISE
# =========================================================
st.markdown("""
<div class="section-title">One Last Little Surprise</div>
<div class="section-subtitle">
    There's something I want you to remember.
</div>
""", unsafe_allow_html=True)

_, promise_col, _ = st.columns([1, 2, 1])

with promise_col:
    if st.button(
        "❤️ Click for a Little Promise",
        use_container_width=True,
    ):
        st.session_state.final_reveal = (
            not st.session_state.final_reveal
        )

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

        <p>
            Forever yours,<br>
            <strong>{html.escape(YOUR_NAME)}</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 13. FOOTER
# =========================================================
st.markdown(f"""
<div class="footer">
    Made with ♡, especially for {html.escape(HER_NAME)}<br>
    <span style="color:#f3d99b;">
        Every love story is special. Ours is my favourite.
    </span>
</div>
""", unsafe_allow_html=True)
