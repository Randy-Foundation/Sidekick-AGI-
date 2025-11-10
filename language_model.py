from problem_solver import problem_solver

import os
import json

class LanguageModel:
    def __init__(self, model_dir="/storage/emulated/0/Sidekick Project Files", gpt_learning_file="gpt_learning.json"):
        """ Initialize Sidekick's local GPT-2 learning process. """
        self.model_dir = model_dir
        self.gpt_learning_file = os.path.join(self.model_dir, gpt_learning_file)
        self.gpt_learning = self._load_gpt_learning()

    def log_trace(self, message):
        """ Logs debug messages to a trace file for analysis. """
        trace_file = os.path.join(self.model_dir, "trace_log.txt")
        with open(trace_file, "a") as file:
            file.write(f"[TRACE] {message}\n")

    def _load_gpt_learning(self):
        """ Load stored learning. """
        if os.path.isfile(self.gpt_learning_file):
            try:
                with open(self.gpt_learning_file, "r") as file:
                    return json.load(file) if isinstance(json.load(file), dict) else {}
            except json.JSONDecodeError:
                return {}
        return {}

    def store_gpt_learning(self, prompt, response):
        """ Store learned responses correctly, avoiding error messages. """
        if "GPT-2 execution failed" in response:
            self.log_trace("⚠ Ignoring failed GPT-2 response, not storing.")
            return  

        self.log_trace(f"✅ Storing learned response: {response}")
        self.gpt_learning[prompt] = response
        with open(self.gpt_learning_file, "w") as file:
            json.dump(self.gpt_learning, file, indent=4)

    def generate_response(self, prompt):
        """ Generate response using stored knowledge first, then learn if needed. """
        prompt = prompt.lower().strip()
        self.log_trace(f"Processing input: '{prompt}'")

        # ✅ Check stored responses
        if prompt in self.gpt_learning:
            self.log_trace(f"✅ Found stored response: {self.gpt_learning[prompt]}")
            return self.gpt_learning[prompt]

        # ❌ No response? Extract pattern and generate a new one.
        response = self.extract_pattern_from_gpt_files(prompt)

        # ✅ Store the new response
        self.store_gpt_learning(prompt, response)

        return response

    def extract_pattern_from_gpt_files(self, prompt):
        """ Extracts a response pattern based on Sidekick's retained GPT files. """
        self.log_trace(f"🔍 Extracting pattern from GPT files for: {prompt}")
        
        # Attempt to match known patterns from stored data
        for key in self.gpt_learning:
            if key in prompt:
                self.log_trace(f"✅ Pattern match found for: {key}")
                return self.gpt_learning[key]

        # Default response
        return f"[Sidekick] I'm still learning, but I'll remember this!"

# Example Usage
if __name__ == "__main__":
    language_model = LanguageModel()
    response = language_model.generate_response("hello sidekick i am creator")
    print(f"Response: {response}")