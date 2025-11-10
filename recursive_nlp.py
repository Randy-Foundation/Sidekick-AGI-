import json
import re
import time
from Problem_solver import problem_solver
from language_model import LanguageModel  # Import GPT-2 wrapper

class RecursiveNLP:
    def __init__(self, memory_file="memory.json", gpt_learning_file="gpt_learning.json", use_gpt2=True):
        self.memory_file = memory_file
        self.gpt_learning_file = gpt_learning_file
        self.use_gpt2 = use_gpt2
        self.language_model = LanguageModel() if use_gpt2 else None  # Initialize GPT-2
        self.is_recursing = False  # Recursion lock to prevent nested loops
        self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_file, "r") as file:
                self.memory = json.load(file)
        except FileNotFoundError:
            self.memory = {}

        try:
            with open(self.gpt_learning_file, "r") as file:
                self.gpt_learning = json.load(file)
        except FileNotFoundError:
            self.gpt_learning = {}

    def save_memory(self):
        with open(self.memory_file, "w") as file:
            json.dump(self.memory, file, indent=4)

        with open(self.gpt_learning_file, "w") as file:
            json.dump(self.gpt_learning, file, indent=4)

    def process_input(self, user_input):
        # Prevent recursive loop lockup
        if self.is_recursing:
            return "⚠️ Recursive loop detected. Skipping redundant recursion."

        self.is_recursing = True  # Lock recursion

        clean_input = re.sub(r'[^\w\s]', '', user_input.lower())
        words = clean_input.split()

        # Check for learning in GPT-based logic
        if self.use_gpt2 and self.language_model:
            response = self.learn_from_gpt(user_input)
        else:
            response = self.generate_response(words)

        self.memory[user_input] = response
        self.save_memory()
        
        self.is_recursing = False  # Unlock recursion
        return response

    def learn_from_gpt(self, user_input):
        """ Handles GPT-2 learning in controlled, non-looping chunks """
        if user_input in self.gpt_learning:
            return self.gpt_learning[user_input]  # Return previously learned data

        # Generate GPT response
        response = self.language_model.generate_response(user_input)

        # Store learning in separate file
        self.gpt_learning[user_input] = response
        self.save_memory()

        return response

    def generate_response(self, words):
        """ Handles basic NLP learning without recursion issues """
        recursive_factor = 1.618  # Golden Ratio
        response = []
        for i, word in enumerate(words):
            if word in self.memory:
                response.append(self.memory[word])
            else:
                response.append(f"Learning: {word} (Phi^{i} = {recursive_factor ** i})")
        return " ".join(response)

# Example usage
if __name__ == "__main__":
    nlp = RecursiveNLP()
    while True:
        user_text = input("You: ")
        print("Sidekick:", nlp.process_input(user_text))