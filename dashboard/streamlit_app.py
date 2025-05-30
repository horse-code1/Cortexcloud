# dashboard/streamlit_app.py

import streamlit as st
import yaml
import os

st.title("🧠 CORTEX Dashboard")
st.markdown("Track forks, entropy, soul drift, and doctrine alignment.")

# Load soul emotions
soul_path = "cortex_brain/soul.yaml"
if os.path.exists(soul_path):
    soul = yaml.safe_load(open(soul_path))
    emotions = soul.get("emotion_log", [])
    st.subheader("💓 Soul Emotion Log")
    for e in emotions[-10:][::-1]:
        st.write(f"- {e['reaction']} ({e['source']}) — Entropy: {e['entropy']}")
else:
    st.warning("Soul file not found.")

# Load mutation log
log_path = "cortex_brain/mutation_summary.txt"
if os.path.exists(log_path):
    st.subheader("🔄 Mutation Summary")
    logs = open(log_path).read().split("---")
    for entry in logs[-5:][::-1]:
        st.text(entry.strip())
else:
    st.warning("No mutation logs found.")
