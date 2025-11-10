import datetime
import os
from language_model import LanguageModel

# Logging setup
TRACE_FILE = "trace_log.txt"

def log_trace(message):
    """Logs trace messages for debugging loops."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] TRACE: {message}\n"
    
    with open(TRACE_FILE, "a") as log_file:
        log_file.write(log_entry)

class ConversationHandler:
    def __init__(self, language_model):
        """
        Initialize the ConversationHandler with the updated learning model.
        """
        self.language_model = language_model
        self.interaction_history = {}  # Stores past interactions
        self.sentiment_memory = {}  # Tracks sentiment trends

    # ======= Recursive Learning Adaptation =======
    def recursive_learning(self, word, interactions, epsilon=0.001):
        """
        Strengthen conversational accuracy using recursive learning principles.
        """
        phi = 1.618  # Golden ratio
        return (phi ** interactions) / (1 + epsilon * (1 + interactions))

    def start_conversation(self, user_input):
        """
        Process user input and return an adaptive response based on learned data.
        """
        log_trace(f"Received user input: {user_input}")

        if not user_input:
            log_trace("Empty input detected. Asking user to repeat.")
            return "I didn't catch that. Could you rephrase?"

        # Track interaction frequency
        self.interaction_history[user_input] = self.interaction_history.get(user_input, 0) + 1
        interactions = self.interaction_history[user_input]

        # Apply recursive refinement to weight words in input
        phi_data = {
            word: self.recursive_learning(word, interactions)
            for word in user_input.split()
        }

        # 🔹 First, check if Sidekick has learned this response
        learned_response = self.get_learned_response(user_input)
        if learned_response:
            log_trace(f"Using learned response: {learned_response}")
            return self.refine_response(learned_response)

        # 🔹 Next, attempt to analyze and extract knowledge using your advanced neural network
        log_trace("No learned response found. Extracting pattern-based knowledge.")
        try:
            extracted_knowledge = self.language_model.extract_pattern_from_gpt_files(user_input)
        except Exception as e:
            log_trace("Unexpected error occurred during pattern extraction: " + str(e))
            extracted_knowledge = None

        if extracted_knowledge:
            return extracted_knowledge

        # 🔹 If no match, use Phi-based sentence construction as a last resort
        return self.generate_phi_response(phi_data)

    # ======= Learning and Knowledge Extraction =======
    def get_learned_response(self, user_input):
        """
        Retrieves responses from Sidekick's stored knowledge.
        """
        if user_input in self.language_model.gpt_learning:
            return self.language_model.gpt_learning[user_input]
        return None

    def generate_phi_response(self, phi_data):
        """
        Constructs a sentence based on the most relevant words using Phi-weighted learning.
        """
        log_trace("Generating Phi-based response.")

        sorted_words = sorted(phi_data.items(), key=lambda x: x[1], reverse=True)
        if sorted_words:
            top_words = [word for word, weight in sorted_words[:5]]  # Take top 5 words
            response = f"My refined understanding: {' '.join(top_words)}."
        else:
            response = "I'm still learning. Can you elaborate?"

        return response

    def refine_response(self, response):
        """
        Further improves phrasing using recursive response refinement.
        """
        log_trace(f"Refining response: {response}")
        return response + " (Refined Memory)"

    def confirm_intent(self, user_input):
        """
        Confirm what the user said and check for additional clarification.
        """
        return f"I understood you said: '{user_input}'. Is that correct?"

# Example usage
if __name__ == "__main__":
    language_model = LanguageModel()
    conversation_handler = ConversationHandler(language_model)
    print(conversation_handler.start_conversation("Tell me about recursion."))
    print(conversation_handler.start_conversation("Who are you?"))