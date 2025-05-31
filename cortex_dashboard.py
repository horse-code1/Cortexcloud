# cortex_dashboard.py

import os
import yaml
import time
from modules.config_loader import load_brain
from modules.cortex_reflector import reflect_if_needed
from cortex_doctrine_mutator import mutate_doctrine

FORKS_DIR = "cortex_brain/forks"

def get_latest_fork():
    forks = sorted([f for f in os.listdir(FORKS_DIR) if f.startswith("Fork_")])
    return forks[-1] if forks else None

def summarize_doctrine(fork_name):
    path = os.path.join(FORKS_DIR, fork_name, "CORTEX_DOCTRINE.md")
    if not os.path.exists(path): return "No doctrine found."
    with open(path, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        return '\n'.join(lines[:3])

def get_last_input(fork_name):
    path = os.path.join(FORKS_DIR, fork_name, "interaction_log.md")
    if not os.path.exists(path): return "No interactions logged."
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in reversed(lines):
            if line.startswith("YOU:"):
                return line.strip()
    return "No user input found."

def get_reflection_status(fork_name):
    path = os.path.join(FORKS_DIR, fork_name, "reflection_log.md")
    if not os.path.exists(path): return "No reflections logged."
    with open(path, 'r') as f:
        lines = f.readlines()
        return lines[-1].strip() if lines else "Empty reflection log."

def display_dashboard(fork_name):
    print("\n🌿 CORTEX Fork Dashboard")
    print("="*60)
    brain = load_brain(os.path.join(FORKS_DIR, fork_name))
    soul = brain.get("soul.yaml", {})
    traits = soul.get("personality_vector", {})

    print(f"🔹 Active Fork: {fork_name}")
    print(f"  Generation: {brain.get('fork_meta.yaml', {}).get('generation', 'N/A')}")
    print(f"  Entropy: {brain.get('runtime_state.yaml', {}).get('entropy', 'N/A')}")
    print(f"  Curiosity: {traits.get('curiosity', 0.5)} | Boldness: {traits.get('boldness', 0.5)} | Empathy: {traits.get('empathy', 0.5)}")

    print("\n🧠 Doctrine Beliefs:")
    print(summarize_doctrine(fork_name))

    print("\n📓 Last User Input:")
    print(get_last_input(fork_name))

    print("\n🪞 Last Reflection:")
    print(get_reflection_status(fork_name))

    print("\n📊 Fork Stats:")
    forks = sorted([f for f in os.listdir(FORKS_DIR) if f.startswith("Fork_")])
    print(f"  Total forks: {len(forks)}")
    print(f"  Most recent: {forks[-1] if forks else 'None'}")
    print("="*60)

def menu():
    latest = get_latest_fork()
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        display_dashboard(latest)

        print("\n🛠 Actions:")
        print("[1] Talk to Fork")
        print("[2] Run Think Loop")
        print("[3] Mutate Doctrine Now")
        print("[4] Visualize Fork Tree")
        print("[5] Switch Fork")
        print("[Q] Quit")

        choice = input("Select an option: ").strip().lower()

        if choice == '1':
            os.system(f"python3 cortex_ai_console.py")
        elif choice == '2':
            os.system(f"python3 main.py {latest}")
            mutate_doctrine(get_latest_fork())  # ✅ Auto-mutate new fork
            input("\n✅ Fork mutated post-creation. Press Enter to continue...")
        elif choice == '3':
            mutate_doctrine(latest)
            input("\n✅ Doctrine mutated. Press Enter to continue...")
        elif choice == '4':
            os.system("python3 cortex_tree_visual.py")
            input("\n🌱 Tree generated. Press Enter to continue...")
        elif choice == '5':
            new_fork = input("Enter new fork name (e.g., Fork_003): ").strip()
            if os.path.exists(os.path.join(FORKS_DIR, new_fork)):
                latest = new_fork
            else:
                input("❌ Fork not found. Press Enter to continue...")
        elif choice == 'q':
            break
        else:
            input("❓ Invalid choice. Press Enter to try again...")

if __name__ == "__main__":
    menu()
