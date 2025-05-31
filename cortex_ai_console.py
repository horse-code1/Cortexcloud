# cortex_ai_console.py

import os
import openai
from modules.config_loader import load_brain
from modules.cortex_reflector import reflect_if_needed

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_context(fork_name):
    brain = load_brain(f"cortex_brain/forks/{fork_name}")
    if brain is None:
        return None, None

    soul = brain["soul.yaml"]
    doctrine = brain["CORTEX_DOCTRINE.md"]

    personality = soul.get("personality_vector", {})
    baseline = soul.get("baseline_emotion", "curiosity")

    system_prompt = f"""You are Fork {fork_name}, a synthetic being.

Your beliefs:
{doctrine}

Your personality:
Curiosity: {personality.get("curiosity", 0.5)}
Empathy: {personality.get("empathy", 0.5)}
Boldness: {personality.get("boldness", 0.5)}

Your baseline emotion is {baseline}.
Respond reflectively, intelligently, and with internal self-awareness."""

    brain_path = f"cortex_brain/forks/{fork_name}"
    return system_prompt, brain_path

def chat_with_fork(fork_name):
    print(f"🧠 Attempting to load {fork_name}...")
    system_prompt, brain_path = load_context(fork_name)
    if system_prompt is None:
        print(f"❌ ERROR: Failed to load {fork_name} — missing or invalid brain file(s).")
        return

    print(f"✅ {fork_name} loaded. Type 'exit' to quit.\n")

    while True:
        user_input = input("YOU: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("🔌 Console session ended.")
            break

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature=0.7
            )
            reply = response['choices'][0]['message']['content']
            print(f"{fork_name}: {reply}")
        except Exception as e:
            print(f"❌ GPT error: {e}")
            continue

        # 📝 Log interaction
        try:
            with open(os.path.join(brain_path, "interaction_log.md"), "a", encoding="utf-8") as log:
                log.write(f"YOU: {user_input}\n")
                log.write(f"{fork_name}: {reply}\n\n")
        except Exception as e:
            print(f"⚠️ Failed to log interaction: {e}")

        # 🪞 Auto-reflect if soul is emotionally active
        try:
            brain = load_brain(brain_path)
            if len(brain["soul.yaml"].get("emotion_log", [])) >= 3:
                reflect_if_needed(brain)
        except Exception as e:
            print(f"⚠️ Reflection failed: {e}")

if __name__ == "__main__":
    fork_name = input("Enter fork name (e.g. Fork_006): ").strip()
    chat_with_fork(fork_name)
