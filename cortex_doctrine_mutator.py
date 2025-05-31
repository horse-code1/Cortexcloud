# cortex_doctrine_mutator.py

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

def mutate_doctrine(fork_name):
    base = f"cortex_brain/forks/{fork_name}"
    doctrine = load_file(os.path.join(base, "CORTEX_DOCTRINE.md"))
    interaction_log = load_file(os.path.join(base, "interaction_log.md"))

    prompt = f"""
You are an evolving synthetic agent with a doctrine guiding your thoughts.
This is your current doctrine:

{doctrine}

This is your interaction log:

{interaction_log}

Based on recent dialogue, propose a new version of your doctrine with up to 3 adjusted or evolved beliefs.
Format it in clean Markdown.
"""

    print("🧬 Requesting GPT-4 doctrine mutation based on conversation...")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    new_doctrine = response['choices'][0]['message']['content']
    save_file(os.path.join(base, "CORTEX_DOCTRINE.md"), new_doctrine)

    with open(os.path.join(base, "reflection_log.md"), "a", encoding="utf-8") as log:
        log.write("🧠 Doctrine updated via conversational pressure:\n")
        log.write(new_doctrine + "\n\n")

    print("✅ Doctrine updated + logged.")

if __name__ == "__main__":
    fork = input("Fork to mutate doctrine: ").strip()
    mutate_doctrine(fork)
