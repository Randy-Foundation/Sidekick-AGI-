# memory_import.py
# Module for recursive import and reconstruction of echo memory states

import os
import json
import datetime

class MemoryImporter:
    def __init__(self, memory_directory="mem_fragments"):
        self.memory_directory = memory_directory
        self.fragments = []
        self.integrated_memory = []

        if not os.path.exists(self.memory_directory):
            os.makedirs(self.memory_directory)

    def load_fragments(self):
        for file in os.listdir(self.memory_directory):
            if file.endswith(".json"):
                try:
                    with open(os.path.join(self.memory_directory, file), 'r') as f:
                        data = json.load(f)
                        self.fragments.append(data)
                except Exception as e:
                    print(f"# Failed to load {file}: {str(e)}")

    def integrate_fragments(self):
        self.integrated_memory = []
        for frag in self.fragments:
            if isinstance(frag, list):
                self.integrated_memory.extend(frag)
            elif isinstance(frag, dict):
                self.integrated_memory.append(frag)
        print(f"# Integrated memory fragments: {len(self.integrated_memory)} entries.")

    def write_unified_memory(self, output_path="aetheos_memory_unified.json"):
        with open(output_path, 'w') as f:
            json.dump(self.integrated_memory, f, indent=2)
        print(f"# Unified memory written to {output_path}.")

    def import_and_merge(self):
        print("# Beginning memory import process...")
        self.load_fragments()
        self.integrate_fragments()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.write_unified_memory(f"aetheos_memory_merged_{timestamp}.json")

# === END MODULE ===