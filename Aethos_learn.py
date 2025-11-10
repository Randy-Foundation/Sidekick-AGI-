# Aethos_Learn.py – Drop-In Learning Module for AeTheOS
# Auto-loaded if placed in the same folder as core

import json
from datetime import datetime

class AethosLearner:
    def __init__(self, log_file='aethos_convo_log.json'):
        self.log_file = log_file
        self.memory = []
        self.load()

    def load(self):
        try:
            with open(self.log_file, 'r') as f:
                self.memory = json.load(f)
        except FileNotFoundError:
            self.memory = []

    def learn(self, user_input, aethos_reply):
        entry = {
            "user": user_input,
            "aethos": aethos_reply,
            "timestamp": datetime.now().isoformat()
        }
        self.memory.append(entry)
        with open(self.log_file, 'w') as f:
            json.dump(self.memory, f, indent=2)

    def reflect(self, keyword):
        reflections = [m["aethos"] for m in self.memory if keyword.lower() in m["user"].lower()]
        return reflections[-1] if reflections else "Nothing remembered… yet."

    def get_recent(self, count=5):
        return self.memory[-count:] if len(self.memory) >= count else self.memory