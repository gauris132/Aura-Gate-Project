import streamlit as st
import time

# --- AURA-GATE CONFIG ---
st.set_page_config(page_title="Aura-Gate AI", layout="centered")

# Custom CSS for the "Vibe" shift
def apply_style(mood):
    if mood == "Panic":
        st.markdown("<style>.stApp { background-color: #e3f2fd; }</style>", unsafe_allow_html=True) # Calm Blue
    elif mood == "Impulse":
        st.markdown("<style>.stApp { background-color: #fff3e0; }</style>", unsafe_allow_html=True) # Warning Orange

st.title("🛡️ Aura-Gate: Emotional Liquidity Layer")
st.write("First-Principles AI for Human-Centered Finance.")

# --- THE PROBLEM STATEMENT CONTEXT ---
# Addressing behavioral biases like Panic Selling and Impulse Investing [cite: 20, 21]
st.sidebar.header("System Status")
st.sidebar.info("Monitoring: Intent & Behavioral Context")

# --- EMOTION DETECTION ENGINE ---
user_text = st.text_input("What's your financial move right now?", placeholder="e.g., 'The market is crashing, I need to sell!'")

# logic for high-impact financial decisions [cite: 30]
panic_words = ["sell", "crash", "scared", "lose", "emergency", "debt", "panic"]
impulse_words = ["buy", "need", "must", "hype", "fomo", "fast", "all in"]

detected_mood = "Neutral"
if any(word in user_text.lower() for word in panic_words):
    detected_mood = "Panic"
elif any(word in user_text.lower() for word in impulse_words):
    detected_mood = "Impulse"

# --- DYNAMIC RESPONSE (THE 'GATES') ---
if detected_mood == "Panic":
    apply_style("Panic")
    st.error("🚨 HIGH ANXIETY DETECTED")
    st.subheader("Calm Protocol Activated")
    st.write("Research shows panic leads to poor outcomes[cite: 18]. We've temporarily paused 'Sell' buttons to protect your portfolio.")
    st.info("Goal: Shift from Amygdala (Fear) to Prefrontal Cortex (Logic).")
    st.button("Start 1-Minute Calm-Down Nudge")

elif detected_mood == "Impulse":
    apply_style("Impulse")
    st.warning("⚡ IMPULSE BIAS DETECTED")
    st.subheader("Logic Gate Activated")
    st.write("Overconfidence during bullish cycles can be risky[cite: 24].")
    reason = st.text_area("To unlock the 'Buy' button, please write a 1-sentence justification for this trade:")
    if len(reason.split()) < 8:
        st.button("Unlock Transaction", disabled=True)
        st.caption("Write at least 8 words to engage your rational thinking.")
    else:
        st.button("Verify & Proceed")

else:
    st.success("✅ Rational State Detected")
    st.button("Proceed to Dashboard")

# --- FOOTER ---
st.divider()
st.caption("Aura-Gate Prototype | Developed for SHARE IITK Global Case Competition")
