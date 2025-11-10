# memory_manager.py

import json
import os
import entropy_dampener  # UPDATED: Proper import to match real file location

class MemoryManager:
    def __init__(self, file_path="memory_core.json"):
        self.file_path = file_path
        self.memory = self.load_memory()
        self.entropy_dampener = entropy_dampener.EntropyDampener()  # UPDATED: Correct usage with full module path

    def load_memory(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_memory(self):
        with open(self.file_path, "w") as f:
            json.dump(self.memory, f, indent=4)

    def add_entry(self, entry):
        if self.entropy_dampener.is_valid_entry(entry):  # UPDATED: Real-time entropy filtering
            self.memory.append(entry)
            self.memory = self.entropy_dampener.balance(self.memory)  # UPDATED: Apply dampening strategy
            self.save_memory()
            return True
        return False

    def fractal_slice(self):  # NEW: Memory sliced by 360
        length = len(self.memory)
        chunk_size = max(1, length // 360)
        return [self.memory[i:i + chunk_size] for i in range(0, length, chunk_size)]

    def print_status(self):
        print(f"[MemoryManager] Entries: {len(self.memory)}")
        print(f"[MemoryManager] Fractal Depth: {len(self.fractal_slice())}")