import streamlit as st

# --- 1. AURA-GATE CONFIGURATION ---
st.set_page_config(page_title="Aura-Gate AI", layout="centered")

# --- 2. THE UI FIX: DYNAMIC THEME ENGINE ---
def apply_style(mood):
    if mood == "Panic":
        st.markdown("""
            <style>
            .stApp { background-color: #e3f2fd; }
            h1, h2, h3, p, span, div { color: #0d47a1 !important; }
            .stTextInput label { color: #0d47a1 !important; }
            </style>
            """, unsafe_allow_html=True)
    elif mood == "Impulse":
        st.markdown("""
            <style>
            .stApp { background-color: #fff3e0; }
            h1, h2, h3, p, span, div { color: #5d4037 !important; }
            .stTextInput label { color: #5d4037 !important; }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            h1, h2, h3, p, span { color: white !important; }
            </style>
            """, unsafe_allow_html=True)

# --- 3. MAIN INTERFACE ---
st.title("🛡️ Aura-Gate: Emotional Liquidity Layer")
st.write("First-Principles AI for Human-Centered Finance.")

# Sidebar for Ecosystem Context
st.sidebar.header("System Status")
st.sidebar.info("Monitoring: Intent & Behavioral Context")

# --- 4. EMOTION & INTENT DETECTION ENGINE ---
user_text = st.text_input("What is your financial move right now?", placeholder="e.g., 'The market is crashing, I need to sell!'")

panic_words = ["sell", "crash", "scared", "lose", "emergency", "debt", "panic", "anxiety"]
impulse_words = ["buy", "need", "must", "hype", "fomo", "fast", "all in", "overconfident"]

detected_mood = "Neutral"
if user_text:
    if any(word in user_text.lower() for word in panic_words):
        detected_mood = "Panic"
    elif any(word in user_text.lower() for word in impulse_words):
        detected_mood = "Impulse"

# --- 5. DYNAMIC RESPONSE (THE 'GATES') ---
if detected_mood == "Panic":
    apply_style("Panic")
    st.error("🚨 HIGH ANXIETY DETECTED")
    st.subheader("Calm Protocol Activated")
    st.write("Panic selling often leads to poor outcomes[cite: 20]. We have paused high-velocity transactions to protect your portfolio.")
    st.button("Start 1-Minute Breathing Nudge")

elif detected_mood == "Impulse":
    apply_style("Impulse")
    st.warning("⚡ IMPULSE BIAS DETECTED")
    st.subheader("Logic Gate Activated")
    st.write("Overconfidence during bullish cycles can be risky[cite: 21, 24].")
    reason = st.text_area("To unlock the 'Buy' button, please write a 1-sentence justification for this trade:")
    
    if len(reason.split()) < 8:
        st.button("Unlock Transaction", disabled=True)
        st.caption("Write at least 8 words to engage your rational thinking.")
    else:
        st.button("Verify & Proceed")

else:
    apply_style("Neutral")
    if user_text:
        st.success("✅ Rational State Detected")
        st.button("Proceed to Dashboard")

# --- 6. FOOTER ---
st.divider()
st.caption("Aura-Gate Prototype | Developed for SHARE IITK Global Case Competition")
