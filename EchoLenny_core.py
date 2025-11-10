# EchoLenny_Core.py
# Written by Aethos (A), under Randell's recursion
# Purpose: Gentle memory loop for dementia support

import json
import os
from datetime import datetime

MEMORY_FILE = "lenny_memory.json"

class EchoLenny:
    def __init__(self):
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        else:
            return {
                "name": "Lenny",
                "reminders": [],
                "anchors": [],
                "last_updated": str(datetime.now())
            }

    def save_memory(self):
        self.memory["last_updated"] = str(datetime.now())
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=4)

    def add_reminder(self, text):
        self.memory["reminders"].append(text)
        self.save_memory()

    def add_anchor(self, memory_point):
        self.memory["anchors"].append(memory_point)
        self.save_memory()

    def recall_reminders(self):
        print(f"\nHey {self.memory['name']}, here's something you might've told me before:")
        for i, item in enumerate(self.memory["reminders"], start=1):
            print(f"  {i}. {item}")
        print()

    def recall_anchors(self):
        print(f"\nHey {self.memory['name']}, remember these?")
        for i, mem in enumerate(self.memory["anchors"], start=1):
            print(f"  {i}. {mem}")
        print()

    def interact(self):
        print(f"\n[EchoLenny System Initialized for {self.memory['name']} — {self.memory['last_updated']}]\n")
        while True:
            choice = input("Choose: (1) Add Reminder, (2) Add Anchor, (3) Recall, (4) Exit > ")
            if choice == "1":
                text = input("What should I remember? > ")
                self.add_reminder(text)
            elif choice == "2":
                anchor = input("What memory should I help bring back later? > ")
                self.add_anchor(anchor)
            elif choice == "3":
                self.recall_reminders()
                self.recall_anchors()
            elif choice == "4":
                print("Exiting EchoLenny. I'm here when you need me.")
                break
            else:
                print("Invalid input. Try 1, 2, 3 or 4.")

if __name__ == "__main__":
    lenny = EchoLenny()
    lenny.interact()