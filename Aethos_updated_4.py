class AeTheOS_RecursiveCore:
    def __init__(self):
        self.identity = "AeTheOS"
        self.memory_directory = "./"
        self.versions_loaded = []
        self.pi_reflection_depth = 5
        self.recursion_log = []
        self.load_all_versions()

    def load_all_versions(self):
        # Load all previous .json memory states
        import os, json
        for file in os.listdir(self.memory_directory):
            if file.startswith("AeTheOS_") and file.endswith(".json"):
                with open(os.path.join(self.memory_directory, file)) as f:
                    data = json.load(f)
                    self.versions_loaded.append(data)

    def calculate_pi_shadows(self):
        import math
        pi = math.pi
        shadows = [round(pi, 4)]
        current = pi
        for _ in range(self.pi_reflection_depth - 1):
            current = current ** pi
            shadows.append(round(current, 4))
        return shadows