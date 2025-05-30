# modules/fingerprint_engine.py

import hashlib

def hash_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

def hash_brain_state():
    print("🔐 Fingerprinting CORTEX brain files...")
    important = [
        "soul.yaml", "ethics.yaml", "core_context.md",
        "CORTEX_DOCTRINE.md", "scoring_config.yaml"
    ]
    for file in important:
        path = f"cortex_brain/{file}"
        hash_val = hash_file(path)
        print(f"{file}: {hash_val[:12]}...")
