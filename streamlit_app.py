import streamlit as st
import time

# --- 1. AURA-GATE CONFIGURATION ---
st.set_page_config(page_title="Aura-Gate Pro", layout="centered")

# Initialize Session Memory for 'Intent Detection'
if 'stress_count' not in st.session_state:
    st.session_state.stress_count = 0

def apply_style(mood):
    if mood == "Panic":
        st.markdown("<style>.stApp { background-color: #e3f2fd; } h1, h2, h3, p, span { color: #0d47a1 !important; }</style>", unsafe_allow_html=True)
    elif mood == "Impulse":
        st.markdown("<style>.stApp { background-color: #fff3e0; } h1, h2, h3, p, span { color: #5d4037 !important; }</style>", unsafe_allow_html=True)

# --- 2. MAIN INTERFACE ---
st.title("🛡️ Aura-Gate Pro: Emotion-Aware AI")
st.sidebar.header("System Settings")
persona = st.sidebar.selectbox("AI Persona", ["The Hostel-Mate", "The Guardian", "The Analyst"])

st.write(f"Current Mode: **{persona}** | Behavioral Context Monitoring Active")

# --- 3. EMOTION & INTENT DETECTION ENGINE ---
# Targets high-impact decisions like panic selling or impulsive investing
user_input = st.text_input("Describe your financial move right now...", placeholder="e.g., 'I am panicking, sell everything!'")

# Behavioral Finance Keywords
panic_words = ["sell", "crash", "scared", "lose", "emergency", "debt", "panic", "anxious", "panicking"]
impulse_words = ["buy", "need", "must", "hype", "fomo", "fast", "all in", "rich"]

if user_input:
    detected_mood = "Neutral"
    if any(word in user_input.lower() for word in panic_words):
        detected_mood = "Panic"
    elif any(word in user_input.lower() for word in impulse_words):
        detected_mood = "Impulse"

    # --- 4. DYNAMIC RESPONSE (THE GATES) ---
    if detected_mood == "Panic":
        st.session_state.stress_count += 1
        apply_style("Panic")
        st.error("🚨 HIGH ANXIETY DETECTED")
        
        # Human-Centered Nudges based on Persona
        if persona == "The Hostel-Mate":
            st.subheader("💬 Hey Gauri, listen to your roomie...")
            st.write("I can tell you're stressed. Let's not empty the account while we're in a panic. I've locked the sell button for a few minutes.")
        else:
            st.subheader("🛡️ Calm Protocol Activated")
            st.write("Avoiding financial planning due to uncertainty leads to poor outcomes. Take a breath.")

        st.info(f"Strategic friction applied. Stress triggers this session: {st.session_state.stress_count}")
        
        if st.button("Launch 1-Minute Breathing Nudge"):
            with st.spinner('Engaging Rational Brain...'):
                time.sleep(3)
            st.success("Rational autonomy restored. Please review your long-term plan.")

    elif detected_mood == "Impulse":
        apply_style("Impulse")
        st.warning("⚡ IMPULSE BIAS DETECTED")
        st.subheader("Logic Gate Activated")
        st.write("Impulsive investing during market hype is a known behavioral bias.")
        
        # Ethical friction to balance user autonomy
        reason = st.text_area("To unlock the trade, justify this move in 10+ words:")
        if len(reason.split()) < 10:
            st.button("Unlock Transaction (Locked)", disabled=True)
            st.caption("Engage your prefrontal cortex by explaining your reasoning.")
        else:
            if st.button("Unlock & Proceed"):
                st.balloons()
                st.success("Rational justification accepted.")

    else:
        st.success("✅ Rational Intent Detected. Proceeding to Dashboard.")

# --- 5. ETHICS & PRIVACY FOOTER ---
st.divider()
st.caption("Aura-Gate Prototype | Developed for SHARE IITK Global Case Competition")
st.caption("Privacy: Emotional and behavioral data is processed in-session and never stored.")
