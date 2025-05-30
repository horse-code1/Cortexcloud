import os
import yaml

def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def read_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_yaml(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False)

def load_brain(folder_path):
    REQUIRED_FILES = [
        "soul.yaml",
        "ethics.yaml",
        "core_context.md",
        "CORTEX_DOCTRINE.md",
        "scoring_config.yaml",
        "runtime_state.yaml",
        "mutation_summary.txt",
        "reflection_log.md",
        "phantom_summary.txt",
        "session_000.md"
    ]

    brain = {}

    for filename in REQUIRED_FILES:
        path = os.path.join(folder_path, filename)
        if not os.path.exists(path):
            print(f"❌ MISSING FILE: {path}")
            return None
        try:
            if filename.endswith(".yaml"):
                with open(path, 'r', encoding='utf-8') as f:
                    yaml.safe_load(f)
        except Exception as e:
            print(f"❌ YAML LOAD ERROR in {filename}: {e}")
            return None

    for filename in REQUIRED_FILES:
        path = os.path.join(folder_path, filename)
        if filename.endswith(".yaml"):
            brain[filename] = read_yaml(path)
        else:
            brain[filename] = load_file(path)

    return brain
