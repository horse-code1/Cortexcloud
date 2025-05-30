# modules/snapshot_engine.py

import os
import shutil
import datetime

def maybe_snapshot(brain):
    flag = brain['runtime_state.yaml'].get("snapshot_on_start", False)
    if not flag:
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    target_dir = f"snapshots/snapshot_{timestamp}"
    os.makedirs(target_dir, exist_ok=True)

    files = os.listdir("cortex_brain")
    for f in files:
        src = os.path.join("cortex_brain", f)
        dst = os.path.join(target_dir, f)
        if os.path.isfile(src):
            shutil.copy2(src, dst)

    print(f"📦 Snapshot saved to {target_dir}")
