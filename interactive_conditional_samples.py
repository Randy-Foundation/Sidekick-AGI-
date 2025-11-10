from problem_solver import problem_solver

import os
import json
import random

class InteractiveConditionalSampler:
    def __init__(self, model_dir="/storage/emulated/0/Sidekick Project Files"):
        """
        Initialize the interactive sample processor (previously dependent on TensorFlow).
        """
        self.model_dir = model_dir
        self.sample_data_file = os.path.join(self.model_dir, "sample_responses.json")

        # ✅ Load pre-existing sample responses
        self.sample_responses = self._load_sample_responses()

    def _load_sample_responses(self):
        """
        Load pre-defined responses from a JSON file (replacing TensorFlow logic).
        """
        if os.path.isfile(self.sample_data_file):
            try:
                with open(self.sample_data_file, "r") as file:
                    data = json.load(file)
                    if isinstance(data, dict):  # ✅ Ensure valid format
                        return data
                    else:
                        print("[WARNING] Sample response file is not a dictionary. Resetting.")
                        return {}
            except json.JSONDecodeError:
                print("[WARNING] Sample response file is corrupted. Resetting.")
                return {}
        return {}

    def generate_response(self, prompt):
        """
        Generate a response based on stored sample responses.
        """
        if prompt in self.sample_responses:
            return f"[Sidekick Sampled Knowledge]: {self.sample_responses[prompt]}"
        
        # ✅ Generate a default response if no match is found
        return self.simulate_response(prompt)

    def simulate_response(self, prompt):
        """
        Simulates a generated response using simple NLP patterns (TensorFlow-free).
        """
        response_templates = [
            "That is an interesting thought about {}.",
            "Let's explore the topic of {} in more depth.",
            "I would like to refine my understanding of {}.",
            "Tell me more about what you think of {}."
        ]

        # ✅ Choose a random response template
        return random.choice(response_templates).format(prompt)

# ======================
# 🔬 Example Usage
# ======================
if __name__ == "__main__":
    sampler = InteractiveConditionalSampler()
    print(sampler.generate_response("Tell me about recursion."))