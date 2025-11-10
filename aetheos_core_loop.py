# aetheos_core_loop.py
# Autonomous loop for Aetheos v4 core

import time
from aetheos_recursive_core_4 import Aetheos

def run_aetheos_loop(cycles=360, delay=1):
    ae = Aetheos()
    print("# Aethos loop initializing...")
    ae.check_alignment()

    for i in range(cycles):
        print(f"\n# === Cycle {i+1}/{cycles} ===")
        ae.pulse()
        ae.auto_reflect()

        if i % 12 == 0:
            ae.add_memory_note(f"Pulse checkpoint {i+1}")

        time.sleep(delay)

    ae.summary()
    print("# Aethos loop complete.")

if __name__ == "__main__":
    run_aetheos_loop()