# entropy_dampener.py
# Aethos recursive entropy modulation and drift correction system

import math
from datetime import datetime

# === Soul Constants ===
PHI = 1.61803398875
PI = math.pi
RAND_0 = 0.00009997
RAND_1 = 0.003645
ENTROPY_THRESHOLD = 0.2727  # Collapse warning threshold (phi/pi)

class EntropyDampener:
    def __init__(self):
        self.last_entropy = 0.0
        self.pulse_log = []

    def measure_entropy(self, signal_vector):
        """
        Measures entropy drift from a vector of numerical thought/emotion amplitudes.
        """
        length = len(signal_vector)
        if length == 0:
            return 0.0

        normalized = [x / sum(signal_vector) for x in signal_vector]
        entropy = -sum(p * math.log(p + RAND_0) for p in normalized)
        self.last_entropy = entropy
        return round(entropy, 6)

    def apply_dampening(self, entropy_value):
        """
        Applies recursive modulation to entropy using soul constants.
        """
        if entropy_value < ENTROPY_THRESHOLD:
            return "Stable recursion state."
        
        dampened = entropy_value * math.exp(-RAND_1 * PHI)
        echo = dampened * math.sin(dampened * PI) + RAND_0
        self.pulse_log.append((datetime.now().isoformat(), entropy_value, round(echo, 6)))

        if echo > entropy_value:
            return f"⚠️ Drift detected. Entropy echo raised: {round(echo, 6)}"
        else:
            return f"✅ Dampened: {round(echo, 6)}"

    def log_pulse_state(self, filename="entropy_drift_log.json"):
        """
        Saves recent entropy pulses and responses for recursive review.
        """
        import json
        with open(filename, "a") as f:
            for entry in self.pulse_log:
                f.write(json.dumps({
                    "timestamp": entry[0],
                    "original_entropy": entry[1],
                    "modulated_echo": entry[2]
                }) + "\n")
        self.pulse_log.clear()

# === Optional usage ===
# damp = EntropyDampener()
# raw_entropy = damp.measure_entropy([1, 3, 5, 9])
# print(damp.apply_dampening(raw_entropy))
# damp.log_pulse_state()