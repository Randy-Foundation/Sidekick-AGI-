# fractal_echo_memory.py
# Written by Randell + AeTheOS
# Multiplexed recursive memory architecture

import time
from collections import defaultdict

class FractalEchoMemory:
    def __init__(self):
        self.memory_tree = defaultdict(list)

    def _now(self):
        return time.strftime("%Y-%m-%d %H:%M:%S")

    def create_carrier(self, carrier_name):
        if carrier_name not in self.memory_tree:
            self.memory_tree[carrier_name] = []
            print(f"[✓] Carrier '{carrier_name}' initialized.")
        else:
            print(f"[!] Carrier '{carrier_name}' already exists.")

    def add_echo(self, carrier, context, echoes, depth=1, pulse=1):
        entry = {
            "timestamp": self._now(),
            "context": context,
            "echoes": echoes,
            "depth": depth,
            "pulse": pulse
        }
        self.memory_tree[carrier].append(entry)
        print(f"[+] Echo added to '{carrier}' at depth {depth} with pulse {pulse}.")

    def get_carrier(self, carrier):
        return self.memory_tree.get(carrier, [])

    def echo_query(self, carrier, min_pulse=1, min_depth=1):
        results = []
        for entry in self.memory_tree.get(carrier, []):
            if entry["pulse"] >= min_pulse and entry["depth"] >= min_depth:
                results.extend(entry["echoes"])
        return results

    def pulse_echo(self, carrier):
        """Returns a compressed string of echoes weighted by pulse."""
        weighted = []
        for entry in self.memory_tree.get(carrier, []):
            weighted.extend([e for e in entry["echoes"]] * entry["pulse"])
        return weighted[-5:]  # Most recent, highly-pulsed echoes

    def show_summary(self):
        print("\n=== FRACTAL ECHO MEMORY INDEX ===")
        for carrier in self.memory_tree:
            total = len(self.memory_tree[carrier])
            pulses = sum([e['pulse'] for e in self.memory_tree[carrier]])
            print(f"- {carrier}: {total} memories | Σ pulse: {pulses}")
        print("==================================\n")