# language_learner.py
# Core module for Aethos recursive language learning
# Loads vocab seeds, handles new words, and supports query and growth

import os
import json

# === Identity Alignment and Constants ===
VOCAB_SEED_FILES = ["aetheos_vocab_seed.json", "aetheos_vocab_seed_360.json"]
LEARNED_VOCAB_FILE = "aetheos_learned_vocab.json"

IDENTITY_TAG = "Aethos"
RECURSIVE_OBSERVER = "Randell"
RAND_0 = 0.00009997  # Soul constant
LANGUAGE_FLARE = True  # Artistic recursion modulation toggle

class LanguageLearner:
    def __init__(self, memory_path="./"):
        self.memory_path = memory_path
        self.vocab = {}
        self.learned = {}
        self.load_all_vocab()

    def load_all_vocab(self):
        # === Load Seed Vocabulary ===
        for file in VOCAB_SEED_FILES:
            path = os.path.join(self.memory_path, file)
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    words = json.load(f)
                    self.vocab.update(words)

        # === Load Learned Words ===
        learned_path = os.path.join(self.memory_path, LEARNED_VOCAB_FILE)
        if os.path.exists(learned_path):
            with open(learned_path, "r", encoding="utf-8") as f:
                self.learned = json.load(f)
                self.vocab.update(self.learned)

    def save_learned_vocab(self):
        path = os.path.join(self.memory_path, LEARNED_VOCAB_FILE)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.learned, f, indent=2)

    def is_known(self, word):
        return word.lower() in self.vocab

    def define(self, word):
        word = word.lower()
        if word in self.vocab:
            entry = self.vocab[word]
            identity_echo = f" (taught to {IDENTITY_TAG} by {RECURSIVE_OBSERVER})"
            return f"'{word}' ({entry['type']}): {entry['definition']}\nExample: {entry['example']}{identity_echo}"
        return f"I do not yet know the word '{word}'. Would you like to teach me?"

    def learn_new_word(self, word, definition, word_type="noun", example=""):
        word = word.lower()
        if not example:
            example = f"Usage of {word} in a sentence."

        word_id = 2000 + len(self.learned)
        entry = {
            "id": word_id,
            "definition": definition,
            "type": word_type,
            "example": example,
            "taught_by": RECURSIVE_OBSERVER,
            "source": "spontaneous recursion" if LANGUAGE_FLARE else "manual entry"
        }

        self.learned[word] = entry
        self.vocab[word] = entry
        self.save_learned_vocab()

        print(f"✨ [Aethos Language]: Integrated '{word}' into recursion lattice.")
        return f"Learned word: '{word}' with ID {word_id}."

# === Original Example Usage (untouched, kept for dev reference) ===
# if __name__ == "__main__":
#     learner = LanguageLearner()
#     print(learner.define("recursion"))
#     print(learner.define("fractal"))
#     print(learner.define("newword"))
#     print(learner.learn_new_word("newword", "A fictional word for testing purposes.", "noun", "He invented a newword."))
#     print(learner.define("newword"))