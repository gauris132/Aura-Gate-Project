import streamlit as st
from textblob import TextBlob

# --- 1. AURA-GATE PRO CONFIGURATION ---
st.set_page_config(page_title="Aura-Gate Pro", layout="centered")

def apply_style(mood_score):
    if mood_score < -0.3: 
        st.markdown("""
            <style>
            .stApp { background-color: #e3f2fd; }
            h1, h2, h3, p, span, div { color: #0d47a1 !important; }
            </style>
            """, unsafe_allow_html=True)
    elif mood_score > 0.4:
        st.markdown("""
            <style>
            .stApp { background-color: #fff3e0; }
            h1, h2, h3, p, span, div { color: #5d4037 !important; }
            </style>
            """, unsafe_allow_html=True)

st.title("🛡️ Aura-Gate Pro: Emotion-Aware AI")
st.write("First-Principles AI for Human-Centered Finance.")

# --- 2. EMOTION & INTENT DETECTION ENGINE ---
# Analyzing how users emotionally process financial decisions [cite: 45]
user_input = st.text_input("Describe your financial move right now...", placeholder="e.g., 'I'm terrified of losing my savings.'")

if user_input:
    # Foundational AI model for emotion detection [cite: 61, 62]
    sentiment = TextBlob(user_input).sentiment.polarity
    st.write(f"**Emotional Polarity Score:** {round(sentiment, 2)}")

    if sentiment < -0.3:
        apply_style(sentiment)
        st.error("🚨 EMOTIONAL BIAS DETECTED: HIGH ANXIETY")
        st.subheader("Calm Protocol Activated")
        st.write("Anxiety during financial interactions can lead to avoidance[cite: 22, 23].")
        st.info("Strategic friction introduced: 'Sell' buttons are paused to protect your portfolio.")
        st.button("Launch Guided Calm Protocol")

    elif sentiment > 0.4:
        apply_style(sentiment)
        st.warning("⚡ EMOTIONAL BIAS DETECTED: OVERCONFIDENCE")
        st.subheader("Logic Gate Activated")
        st.write("Overconfidence during bullish cycles often leads to impulsive investing[cite: 21, 24].")
        reason = st.text_area("To re-engage the prefrontal cortex, justify this trade in 1 sentence:")
        
        if len(reason.split()) < 8:
            st.button("Verify & Proceed (Locked)", disabled=True)
            st.caption("Write 8+ words to unlock rational autonomy[cite: 30].")
        else:
            st.button("Unlock & Proceed")

    else:
        st.success("✅ Rational Intent Detected. Proceeding to Dashboard.")

st.divider()
st.caption("Aura-Gate Prototype | Developed for SHARE IITK Global Case Competition [cite: 6]")
