import streamlit as st
from textblob import TextBlob # New AI Brain

# --- 1. AURA-GATE PRO CONFIG ---
st.set_page_config(page_title="Aura-Gate Pro", layout="centered")

def apply_style(mood_score):
    if mood_score < -0.3: # Negative sentiment detected
        st.markdown("<style>.stApp { background-color: #e3f2fd; } h1, h2, h3, p { color: #0d47a1 !important; }</style>", unsafe_allow_html=True)
    elif mood_score > 0.5: # Over-excitement/Hype detected
        st.markdown("<style>.stApp { background-color: #fff3e0; } h1, h2, h3, p { color: #5d4037 !important; }</style>", unsafe_allow_html=True)

st.title("🛡️ Aura-Gate Pro: Emotion-Aware AI")
st.write("Detecting behavioral context via Sentiment Analysis.") [cite: 30]

# --- 2. THE AI ENGINE ---
user_input = st.text_input("Describe your financial intent...") [cite: 30]

if user_input:
    # Analyzing real emotional polarity 
    sentiment = TextBlob(user_input).sentiment.polarity
    st.write(f"Emotional Polarity Score: {round(sentiment, 2)}")

    if sentiment < -0.3:
        apply_style(sentiment)
        st.error("🚨 EMOTIONAL BIAS: ANXIETY DETECTED") [cite: 22]
        st.info("Aura-Gate is introducing 'Strategic Friction' to prevent panic decisions.") [cite: 30]
        st.button("Start Rational Re-centering")

    elif sentiment > 0.5:
        apply_style(sentiment)
        st.warning("⚡ EMOTIONAL BIAS: EUPHORIA/HYPE") [cite: 21]
        st.write("High confidence detected. Please verify your risk parameters.") [cite: 47]
        st.text_area("Justify this trade (Rational engagement required):")
