import os
import yaml
import openai
from modules.config_loader import load_brain, save_yaml
from modules.cortex_reflector import reflect_if_needed

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_context(fork_name):
    brain = load_brain(f"cortex_brain/forks/{fork_name}")
    if brain is None:
        return None

    soul = brain.get("soul.yaml", {})
    doctrine = brain.get("CORTEX_DOCTRINE.md", "")
    reflection_log = brain.get("reflection_log.md", "")

    context = f"""
You are {soul.get('name', fork_name)}, a synthetic agent with a reflective mind.

Baseline Emotion: {soul.get('baseline_emotion')}
Personality Traits: {soul.get('personality_vector')}
Long-Term Goal: {soul.get('goal_alignment', {}).get('long_term')}
Short-Term Goal: {soul.get('goal_alignment', {}).get('short_term')}

Your current doctrine:
{doctrine}

Recent reflections:
{reflection_log}

Respond thoughtfully and with internal consistency.
"""
    return context

def log_emotion(fork_name, reaction, source, entropy):
    soul_path = f"cortex_brain/forks/{fork_name}/soul.yaml"
    with open(soul_path, 'r') as f:
        soul = yaml.safe_load(f)

    if "emotion_log" not in soul or not isinstance(soul["emotion_log"], list):
        soul["emotion_log"] = []

    soul["emotion_log"].append({
        "reaction": reaction,
        "source": source,
        "entropy": entropy
    })

    save_yaml(soul_path, soul)

def interact_with_fork(fork_name):
    print(f"🧠 Attempting to load {fork_name}...")

    brain = load_brain(f"cortex_brain/forks/{fork_name}")
    if brain is None:
        print(f"❌ ERROR: Failed to load {fork_name} — missing or invalid brain file(s).")
        return

    print(f"✅ Connected to {fork_name}. Type 'exit' to quit.\n")

    log_path = f"cortex_brain/forks/{fork_name}/interaction_log.md"
    if not os.path.exists(log_path):
        with open(log_path, 'w'): pass

    while True:
        context = load_context(fork_name)
        if context is None:
            print("❌ ERROR: Failed to build context. Exiting.")
            return

        user_input = input("YOU: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("🔌 Console session ended.")
            break

        # Detect cognitive triggers
        trigger_reflection = any(word in user_input.lower() for word in [
            "contradiction", "conflict", "paradox", "you're wrong", "inconsistent"
        ])
        if trigger_reflection:
            log_emotion(fork_name, "contradiction", "user_prompt", 0.51)

        messages = [
            {"role": "system", "content": context},
            {"role": "user", "content": user_input}
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature=0.7
            )
            reply = response['choices'][0]['message']['content']
        except Exception as e:
            print("⚠️ GPT ERROR:", e)
            continue

        print(f"{fork_name}: {reply.strip()}\n")

        with open(log_path, "a", encoding="utf-8") as log:
            log.write(f"YOU: {user_input}\n{fork_name}: {reply.strip()}\n\n")

        if trigger_reflection:
            print("🪞 Reflecting on contradiction...")
            reflect_if_needed(brain)
            print("✅ Reflection complete.\n")

if __name__ == "__main__":
    fork = input("Enter fork name (e.g. Fork_005): ")
    interact_with_fork(fork.strip())
