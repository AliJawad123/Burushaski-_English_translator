
import streamlit as st
import streamlit.components.v1 as components
import html

st.set_page_config(
    page_title="For My Jasmine ♡",
    page_icon="🌷",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------- PERSONAL DETAILS ----------------
YOUR_NAME = "Jawad"
HER_NAME = "My Daltas Jasmine"
ANNIVERSARY_DATE = "19 October 2026"

LOVE_LETTER = """
My dearest Jasmine, ♡

Happy six months to us!

These six months have made my life more beautiful.
You have become such a special part of my days,
my thoughts, and the future I dream about.

I may not always find the perfect words to describe
my feelings, but I hope I can spend a lifetime
showing you how much you mean to me.

If I could choose again, I would still choose you.

Thank you for being part of my story.
I cannot wait to write the rest of it with you.

Six months down, a lifetime to go.

Forever yours,
Jawad ♡
"""

REASONS = [
    ("♡", "Your heart", "Your kindness makes everything feel warmer."),
    ("☀", "Your smile", "You make even ordinary days feel special."),
    ("✿", "Your care", "The little things you do mean so much to me."),
    ("☾", "Your mind", "I love the way you think and see the world."),
    ("🦋", "Your presence", "Life feels sweeter with you in it."),
    ("∞", "Simply you", "There is no one else I'd rather choose."),
]

# ---------------- SESSION STATE ----------------
if "opened" not in st.session_state:
    st.session_state.opened = False

if "letter" not in st.session_state:
    st.session_state.letter = False

if "promise" not in st.session_state:
    st.session_state.promise = False

# ---------------- SIMPLE STYLING ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:wght@400;500;600&family=Great+Vibes&display=swap');

.stApp {
    background: linear-gradient(180deg, #fff8f5, #fff0f3);
    color: #654d54;
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"],
footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p {
    color: #654d54;
}

.hero {
    text-align: center;
    padding: 40px 18px;
    border-radius: 24px;
    background: rgba(255,255,255,.72);
    border: 1px solid #f4d9df;
    animation: appear 1s ease;
}

.flower {
    font-size: 2.3rem;
    margin-bottom: 12px;
}

.script {
    font-family: 'Great Vibes', cursive;
    color: #bc718b;
    font-size: clamp(3.3rem, 9vw, 5.5rem);
    line-height: 1.15;
    margin: 16px 0;
}

.subtitle {
    color: #a56c80;
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
}

.small-text {
    color: #927981;
    line-height: 1.9;
    font-size: .95rem;
}

.section-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: #a45f78;
    margin-top: 42px;
    margin-bottom: 8px;
}

.section-subtitle {
    text-align: center;
    color: #a18a91;
    margin-bottom: 22px;
    font-size: .9rem;
}

.reason {
    text-align: center;
    background: rgba(255,255,255,.8);
    border: 1px solid #f2dce2;
    border-radius: 16px;
    padding: 20px 12px;
    min-height: 145px;
    margin-bottom: 12px;
    transition: transform .2s ease;
}

.reason:hover {
    transform: translateY(-4px);
}

.reason-icon {
    font-size: 1.7rem;
    color: #c57894;
}

.reason-title {
    font-family: 'Playfair Display', serif;
    color: #875669;
    font-size: 1.05rem;
    margin: 9px 0;
}

.reason-text {
    color: #907880;
    font-size: .83rem;
    line-height: 1.6;
}

.letter {
    white-space: pre-wrap;
    line-height: 2;
    padding: 25px;
    border: 1px solid #efcfd9;
    border-radius: 18px;
    background: white;
    color: #795b67;
}

.promise {
    text-align: center;
    background: #fff;
    border: 1px solid #f0d4de;
    border-radius: 22px;
    padding: 28px 18px;
}

.promise h2 {
    font-family: 'Great Vibes', cursive;
    font-size: 3rem;
    color: #bb708b;
    font-weight: 400;
}

div[data-testid="stButton"] > button {
    background: #d88da6;
    color: white;
    border: 1px solid #d88da6;
    border-radius: 30px;
    padding: .65rem 1.2rem;
    font-weight: 500;
    transition: .2s ease;
}

div[data-testid="stButton"] > button:hover {
    background: #bd718d;
    border-color: #bd718d;
    color: white;
    transform: translateY(-2px);
}

.footer {
    text-align: center;
    color: #b197a1;
    font-size: .82rem;
    padding-top: 35px;
}

@keyframes appear {
    from {opacity: 0; transform: translateY(12px);}
    to {opacity: 1; transform: translateY(0);}
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- OPENING SCREEN ----------------
if not st.session_state.opened:
    st.markdown("""
    <div class="hero">
        <div class="flower">🌷 ♡ 🌷</div>
        <div class="small-text">A LITTLE SURPRISE FOR YOU</div>
        <div class="script">Once Upon a Time...</div>
        <p class="small-text">
            A story began, two hearts grew closer,<br>
            and six beautiful months passed.<br><br>
            I made something just for you, my love.
        </p>
        <div class="flower">🦋</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    _, button_col, _ = st.columns([1, 1, 1])
    with button_col:
        if st.button("♡  A  ♡", use_container_width=True):
            st.session_state.opened = True
            st.balloons()
            st.rerun()

    st.markdown(
        '<p class="section-subtitle">Click to open your surprise ✨</p>',
        unsafe_allow_html=True
    )
    st.stop()

# ---------------- ANNIVERSARY MESSAGE ----------------
st.markdown(f"""
<div class="hero">
    <div class="flower">🌸</div>
    <div class="small-text">HAPPY HALF-YEAR ANNIVERSARY</div>
    <div class="script">Happy Six Months!</div>
    <div class="subtitle">My dearest {html.escape(HER_NAME)} ♡</div>
    <br>
    <p class="small-text">
        Six months of us, countless little memories,<br>
        and a future I cannot wait to share with you.<br><br>
        You are my favourite part of this story.
    </p>
    <div class="small-text">{html.escape(ANNIVERSARY_DATE)}</div>
</div>
""", unsafe_allow_html=True)

# ---------------- SIX REASONS ----------------
st.markdown("""
<div class="section-title">Six Things I Love About You</div>
<div class="section-subtitle">And a million more I could never fit on this page.</div>
""", unsafe_allow_html=True)

for start in range(0, len(REASONS), 2):
    cols = st.columns(2)
    for col, (icon, title, message) in zip(cols, REASONS[start:start + 2]):
        with col:
            st.markdown(f"""
            <div class="reason">
                <div class="reason-icon">{icon}</div>
                <div class="reason-title">{html.escape(title)}</div>
                <div class="reason-text">{html.escape(message)}</div>
            </div>
            """, unsafe_allow_html=True)

# ---------------- LOVE LETTER ----------------
st.markdown("""
<div class="section-title">A Little Letter for You</div>
<div class="section-subtitle">Something I wanted you to know. 💌</div>
""", unsafe_allow_html=True)

_, col, _ = st.columns([1, 2, 1])
with col:
    if not st.session_state.letter:
        if st.button("💌 Open my letter", use_container_width=True):
            st.session_state.letter = True
            st.rerun()
    else:
        st.markdown(
            f'<div class="letter">{html.escape(LOVE_LETTER)}</div>',
            unsafe_allow_html=True
        )
        if st.button("Close letter", use_container_width=True):
            st.session_state.letter = False
            st.rerun()

# ---------------- FINAL PROMISE ----------------
st.markdown("""
<div class="section-title">One Last Thing...</div>
<div class="section-subtitle">A little promise from my heart to yours.</div>
""", unsafe_allow_html=True)

_, col, _ = st.columns([1, 2, 1])
with col:
    if st.button("♡ One little promise", use_container_width=True):
        st.session_state.promise = not st.session_state.promise

if st.session_state.promise:
    st.balloons()
    st.markdown(f"""
    <div class="promise">
        <div class="flower">♡</div>
        <h2>My Promise to You</h2>
        <p class="small-text">
            I cannot promise every day will be perfect.<br>
            But I promise to keep caring, keep learning,<br>
            and keep choosing us.<br><br>
            I hope we get to celebrate countless more
            anniversaries together.
        </p>
        <h2>Forever Yours</h2>
        <p class="small-text">{html.escape(YOUR_NAME)} ♡</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(f"""
<div class="footer">
    Made with love, just for {html.escape(HER_NAME)} 🌷<br>
    Six months down, a lifetime to go.
</div>
""", unsafe_allow_html=True)
