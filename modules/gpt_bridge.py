# modules/gpt_bridge.py

import os
import yaml
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")



def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def save_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def rewrite_doctrine_for(fork_name):
    fork_path = f"cortex_brain/forks/{fork_name}"
    soul = yaml.safe_load(load_file(f"{fork_path}/soul.yaml"))
    doctrine = load_file(f"{fork_path}/CORTEX_DOCTRINE.md")
    emotion_log = soul.get("emotion_log", [])

    prompt = f"""
You are a synthetic intelligence with a doctrine that guides your beliefs and behavior.
Here is your current doctrine:

{doctrine}

Your emotional history (log of reactions):

{emotion_log}

Based on your emotions, entropy, and personality traits, propose a new version of your doctrine with 1–3 adjusted or evolved beliefs. Keep it markdown-formatted.
"""

    print("🧠 Requesting GPT-driven doctrine mutation...")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    new_doctrine = response['choices'][0]['message']['content']
    save_file(f"{fork_path}/CORTEX_DOCTRINE.md", new_doctrine)

    with open(f"{fork_path}/reflection_log.md", "a", encoding="utf-8") as log:
        log.write("🧬 GPT-generated doctrine update:\n")
        log.write(new_doctrine + "\n\n")

    print(f"✅ {fork_name} doctrine updated + logged.")
