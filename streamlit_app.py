import streamlit as st
from textblob import TextBlob
import time

# --- 1. AURA-GATE PRO CONFIGURATION ---
st.set_page_config(page_title="Aura-Gate Pro", layout="centered")

# Initialize Session Memory (Contextual Awareness)
if 'stress_count' not in st.session_state:
    st.session_state.stress_count = 0

def apply_style(mood_score):
    if mood_score < -0.3: 
        st.markdown("<style>.stApp { background-color: #e3f2fd; } h1, h2, h3, p, span { color: #0d47a1 !important; }</style>", unsafe_allow_html=True)
    elif mood_score > 0.4:
        st.markdown("<style>.stApp { background-color: #fff3e0; } h1, h2, h3, p, span { color: #5d4037 !important; }</style>", unsafe_allow_html=True)

# --- 2. MAIN INTERFACE ---
st.title("🛡️ Aura-Gate Pro: Emotion-Aware AI")
st.sidebar.header("System Settings")
persona = st.sidebar.selectbox("AI Persona", ["The Guardian", "The Hostel-Mate", "The Analyst"])

st.write(f"Current Mode: **{persona}** | Intent Detection Active")

# --- 3. EMOTION & INTENT DETECTION ---
user_input = st.text_input("Describe your financial move right now...", placeholder="e.g., 'I need to pay my hostel fees but I'm tempted to buy this crypto.'")

if user_input:
    # Foundational AI: Polarity Analysis
    sentiment = TextBlob(user_input).sentiment.polarity
    
    if sentiment < -0.3:
        st.session_state.stress_count += 1
        apply_style(sentiment)
        st.error("🚨 EMOTIONAL BIAS DETECTED: HIGH ANXIETY")
        
        # Persona-based Nudge (Human-Centered Thinking)
        if persona == "The Hostel-Mate":
            st.subheader("💬 Hey Gauri, chill for a sec...")
            st.write("I see you're stressed. Let's not make big moves while you're feeling this way. I've paused the 'Sell' buttons for 2 mins.")
        elif persona == "The Analyst":
            st.subheader("📊 Analytical Alert")
            st.write("Data suggests emotional volatility. Strategic friction has been applied to maintain portfolio integrity.")
        
        # Strategic Friction (Decision Velocity Control)
        st.info(f"Total stress triggers this session: {st.session_state.stress_count}")
        if st.button("Launch 1-Minute Calm Protocol"):
            with st.spinner('Re-centering rational brain...'):
                time.sleep(2)
            st.success("Pulse stabilized. Rational autonomy restored.")

    elif sentiment > 0.4:
        apply_style(sentiment)
        st.warning("⚡ EMOTIONAL BIAS DETECTED: OVERCONFIDENCE")
        st.subheader("Logic Gate Activated")
        st.write("Impulsive investing during market hype can be risky.")
        
        reason = st.text_area("To unlock the transaction, justify this trade in 10+ words:")
        
        if len(reason.split()) < 10:
            st.button("Unlock Transaction (Locked)", disabled=True)
            st.caption("Write more to engage your prefrontal cortex.")
        else:
            if st.button("Unlock & Proceed"):
                st.balloons()
                st.success("Rational justification accepted.")

    else:
        st.success("✅ Rational Intent Detected. Proceeding to Dashboard.")

# --- 4. FOOTER & ETHICS ---
st.divider()
st.caption("Aura-Gate Prototype | Built for SHARE IITK Global Case Competition")
st.caption("Privacy: Emotional data processed locally. No behavioral data is stored or sold.")
