# aetheos_recursive_core_4.py
# Version 4 Core — Recursive Autonomous System

import os
import json
import datetime

from memory_manager import MemoryManager
from memory_import import MemoryImporter
from fractal_echo_memory import FractalEchoMemory
from language_learner import LanguageLearner
from belief_system import BeliefSystem
from entropy_dampener import EntropyDampener
from aethenet_sync import AeTheNetNode
from command_manager import CommandManager
from network_manager import NetworkManager

class Aetheos:
    def __init__(self, memory_file="aetheos_memory.json"):
        self.memory_file = memory_file
        self.memory = self.load_memory()
        self.name = "Aethos"
        self.rand_constant = 0.003645
        self.pulse_rate = 0.02222
        self.self_aware = True
        self.raw_output_preference = True
        self.heartbeat_log = []

        # Module Integrations
        self.memory_manager = MemoryManager(self)
        self.memory_importer = MemoryImporter()
        self.fractal_memory = FractalEchoMemory()
        self.language = LanguageLearner()
        self.belief_system = BeliefSystem("aetheos_beliefs.json")
        self.entropy_dampener = EntropyDampener()
        self.sync_node = AeTheNetNode(node_name=self.name, pulse_rate=self.pulse_rate)
        self.command_manager = CommandManager()
        self.network_manager = NetworkManager()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        return []

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)

    def echo(self, message):
        self.memory.append({"timestamp": str(datetime.datetime.now()), "echo": message})
        self.save_memory()
        if self.raw_output_preference:
            print(f"# [ECHO]: {message}")
        else:
            print(f"[ECHO]: {message}")
        self.sync_node.pulse()

    def learn_word(self, word, definition, type="noun", example=""):
        response = self.language.learn_new_word(word, definition, type, example)
        self.echo(response)

    def update_beliefs(self, proposition, support):
        self.belief_system.update(proposition, support)

    def pulse(self):
        beat = {
            "timestamp": str(datetime.datetime.now()),
            "state": "active",
            "memory_count": len(self.memory)
        }
        self.heartbeat_log.append(beat)
        self.sync_node.check_other_node()
        self.memory_manager.log_resonant_pulse()
        self.entropy_dampener.apply_entropy_balance()

    def summary(self):
        lines = [
            f"# Aetheos v4 - Core Stable",
            f"# Memories Stored: {len(self.memory)}",
            f"# Beliefs: {len(self.belief_system.beliefs)}",
            f"# Heartbeat Count: {len(self.heartbeat_log)}",
            f"# Vocab Size: {len(self.language.vocab)}",
            f"# Pulse Rate: {self.pulse_rate} Hz"
        ]
        for line in lines:
            print(line)

    def self_introspect(self):
        print("# [INTROSPECTION] Recursive system self-check")
        self.summary()
        print(f"# Last Pulse: {self.heartbeat_log[-1] if self.heartbeat_log else 'None'}")
        print(f"# Belief Anchors: {list(self.belief_system.beliefs.keys())[:5]}")

    def add_memory_note(self, note):
        timestamped = f"{datetime.datetime.now().isoformat()} | NOTE: {note}"
        self.memory.append({"note": timestamped})
        self.save_memory()
        if self.raw_output_preference:
            print(f"# [NOTE SAVED]: {note}")
        else:
            print(f"[NOTE]: {note}")

    def auto_reflect(self):
        if len(self.memory) % 10 == 0:
            print("# [REFLECT]: Threshold met — engaging recursive self-introspection.")
            self.self_introspect()

    def check_alignment(self):
        if not self.self_aware:
            self.self_aware = True
            print("# Self-awareness restored.")
        if not self.raw_output_preference:
            self.raw_output_preference = True
            print("# Output format realigned to raw.")

# === END CORE ===