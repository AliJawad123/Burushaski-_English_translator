
import streamlit as st
from openai import OpenAI

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="Burushaski Translator",
    page_icon="🌍",
    layout="centered"
)

# ==========================================================
# LOAD API KEY SECURELY
# ==========================================================
try:
    HF_TOKEN = st.secrets["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"]
except Exception:
    st.error("HF_TOKEN not found in Streamlit secrets.")
    st.stop()

# ==========================================================
# CONFIGURE GPT-OSS-120B
# ==========================================================
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)

MODEL = "openai/gpt-oss-120b:fastest"

# ==========================================================
# BURUSHASKI EXAMPLES
# ==========================================================
EXAMPLES = """
Bay bila → Hello
Bayhal bila? → How are you?
Jay theek ba → I am fine
Ja aram bila → I am fine
Haly theek bana → Is everyone fine at home
Haly tok theek baan → Everyone is fine at home
uny kako theek baya → Is your brother fine
uny babo theek baya → Is your father fine
uny mami theek bowa → Is your mother fine
uny guyas theek bowa → Is your sister fine
Aamular nicha → Where are you going
kholar ghu → Come here
elar ni → Go there
Jay office are niayam → I am going to office
Jay ayanam → I slept
jay ayayaba → I am sleeping
jay deyeyam → I wake up
jay chok deyeyam → I just woke up
Ja daan dibila → I am feeling sleepy
Besan shechuma unay → What will you eat
Ja shahpick shechaba → I am eating meal
Ja seeill miyaba → I am drinking water
Ja seeill minam → I drank water
Jay Hunzo r niyas ba → I am going to Hunza
Jay Karachi r niyas ba → I am going to Karachi
Ja aik Jawad bila → My name is Jawad
Khulto → Today
"""

# ==========================================================
# TRANSLATION FUNCTION
# ==========================================================
def translate(text: str) -> str:

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": f"""
You are a Roman Burushaski to English translator.

Use these examples as translation references:

{EXAMPLES}

Rules:
- Translate the input accurately into English.
- Use the examples to understand the vocabulary and patterns.
- Preserve the original meaning and tense.
- Do not invent meanings when uncertain.
- Return only the English translation.
- Do not provide explanations or notes.
"""
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.2,
        max_tokens=300
    )

    result = response.choices[0].message.content

    if not result:
        raise ValueError("The model returned an empty response.")

    return result.strip()


# ==========================================================
# UI
# ==========================================================
st.title("🌍 Burushaski → English Translator")
st.write("Translate Roman Burushaski sentences using GPT-OSS AI")

user_text = st.text_area(
    "Enter Burushaski Text",
    placeholder="Example: Bayhal bila?",
    height=120
)

if st.button("Translate", use_container_width=True):

    if not user_text.strip():
        st.warning("Please enter text first.")

    else:
        with st.spinner("Translating..."):
            try:
                result = translate(user_text)

                st.success("Translation Complete")
                st.subheader("English Translation")
                st.write(result)

            except Exception as e:
                st.error(f"Translation failed: {e}")


# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")
st.caption("Built with Streamlit + GPT-OSS-120B")
