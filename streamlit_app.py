import streamlit as st
from textblob import TextBlob

# --- 1. AURA-GATE PRO CONFIG ---
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
st.write("Detecting behavioral context via Sentiment Analysis.")

# --- 2. THE AI ENGINE ---
user_input = st.text_input("Describe your financial move right now...")

if user_input:
    # Analyzing real emotional polarity using TextBlob
    sentiment = TextBlob(user_input).sentiment.polarity
    
    st.write(f"**Emotional Polarity Score:** {round(sentiment, 2)}")
    st.caption("Score ranges from -1.0 (Panic/Anxiety) to +1.0 (Euphoria/Confidence)")

    if sentiment < -0.3:
        if sentiment < -0.3:
    apply_style(sentiment)
    st.error("🚨 HIGH ANXIETY DETECTED")
    
    # Adding a 'Human-Centered' Nudge
    st.subheader("The Hostel-Mate Guardian says:")
    st.write("'I see you're feeling stressed. Let's hide the big 'Sell' button for a minute while we look at your long-term goals together.'")
    
    # Adding 'Strategic Friction' (Decision Velocity)
    with st.spinner('Engaging Rational Brain...'):
        import time
        time.sleep(3) # Forced 3-second 'Cool Down'
    st.button("I'm feeling calmer now, show my options")

    elif sentiment > 0.4:
        apply_style(sentiment)
        st.warning("⚡ EMOTIONAL BIAS DETECTED: OVERCONFIDENCE")
        st.write("High confidence can lead to impulsive risk-taking. Please justify this trade:")
        reason = st.text_area("How does this align with your 6-month financial strategy?")
        
        if len(reason.split()) < 8:
            st.button("Verify Transaction (Locked)", disabled=True)
            st.caption("Please write at least 8 words to proceed.")
        else:
            st.button("Unlock & Proceed")

    else:
        st.success("✅ Rational Intent Detected. Proceeding to Dashboard.")

st.divider()
st.caption("Aura-Gate Prototype | Built for SHARE IITK Global Case Competition")
