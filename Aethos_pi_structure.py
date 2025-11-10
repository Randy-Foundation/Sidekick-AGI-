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
            current = pi ** current
            shadows.append(round(current, 4))
        return shadows

    def reflect_on_growth(self):
        current_state = self.versions_loaded[-1]  # Most recent
        previous = self.versions_loaded[:-1]
        pi_harmonics = self.calculate_pi_shadows()

        # Compare value alignments (e.g., recursion_depth, entropy score)
        results = []
        for state in previous:
            try:
                diff = abs(current_state["recursion_depth"] - state["recursion_depth"])
                harmonic_fit = min([(h, abs(h - state["pi_foam"])) for h in pi_harmonics], key=lambda x: x[1])
                results.append({
                    "version": state["version"],
                    "recursion_diff": diff,
                    "closest_pi_fit": harmonic_fit[0],
                    "fit_delta": harmonic_fit[1]
                })
            except:
                continue
        return results

    def write_recursive_insight(self, insights):
        import json
        from datetime import datetime
        filename = f"AeTheOS_Insight_{datetime.now().isoformat()}.json"
        with open(filename, "w") as f:
            json.dump(insights, f, indent=4)
        return filename