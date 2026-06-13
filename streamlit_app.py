import streamlit as st
import google.generativeai as genai

# ==========================================================
# API KEY
# ==========================================================

GEMINI_API_KEY = "AQ.Ab8RN6KYWnJGrJdOF7DZ5IV2-_pEfv4b9fyV7hBWwsmwPB6tUA"
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

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
Aamular nicha → where are you going
kholar ghu → come here
elar ni → go there
Jay office are niayam → I am going to office
Jay ayanam → I slept
jay ayayaba → I am sleeping
jay deyeyam → I wake up
jay chok deyeyam → I just woke up
Ja daan dibila → I am feeling sleepy
Besan shechuma unay → what will you eat
Ja shahpick shechaba → I am eating meal
Ja seeill miyaba → I am drinking water
Ja seeill minam → I drunk water
Jay Hunzo r niyas ba → I am going to Hunza
Jay Karachi r niyas ba → I am going to Karachi
Ja aik Jawad bila → my name is Jawad
Khulto → Today
"""

# ==========================================================
# TRANSLATION FUNCTION
# ==========================================================

def translate(text):

    prompt = f"""
You are a Roman Burushaski to English translator.

Use the examples below to understand the language:

{EXAMPLES}

Translate the given Burushaski sentence.

Return ONLY the English translation.

Burushaski: {text}

English:
"""

    response = model.generate_content(prompt)

    return response.text.strip()


# ==========================================================
# STREAMLIT UI
# ==========================================================

st.set_page_config(
    page_title="Burushaski Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Burushaski → English Translator")
st.write(
    "Translate Roman Burushaski sentences into English using Gemini AI."
)

user_text = st.text_area(
    "Enter Burushaski Text",
    height=120,
    placeholder="Example: Bayhal bila?"
)

if st.button("Translate", use_container_width=True):

    if user_text.strip() == "":
        st.warning("Please enter some Burushaski text.")
    else:

        with st.spinner("Translating..."):

            try:
                translation = translate(user_text)

                st.success("Translation Complete")

                st.subheader("English Translation")
                st.write(translation)

            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.caption("Built with Streamlit + Gemini")
