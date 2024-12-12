import re
import json
import random
from datetime import datetime


class LanguageModel:
    def __init__(self):
        # Core Language Processing Components
        self.tone_adaptations = {
            "friendly": ["Hi there!", "How can I help?", "I'm here for you!"],
            "formal": ["Greetings.", "How may I assist you?", "I am at your service."],
            "empathetic": ["I understand how you feel.", "That must be tough.", "I'm here to help."]
        }
        self.default_tone = "friendly"

        # Language and Pattern Recognition
        self.known_patterns = {}
        self.default_responses = ["I'm sorry, I didn't quite catch that.", "Could you clarify that for me?"]

        # Sentiment and Tone History
        self.interaction_history = []

    def process_input(self, user_input):
        """Process and analyze the user's input."""
        sentiment = self.analyze_sentiment(user_input)
        tone = self.determine_tone(user_input)
        self.log_interaction(user_input, sentiment, tone)
        return sentiment, tone

    def analyze_sentiment(self, text):
        """Analyze the sentiment of user input."""
        if re.search(r"(happy|great|awesome|excited)", text, re.IGNORECASE):
            return "positive"
        elif re.search(r"(sad|angry|upset|frustrated)", text, re.IGNORECASE):
            return "negative"
        elif re.search(r"(okay|fine|neutral)", text, re.IGNORECASE):
            return "neutral"
        else:
            return "unknown"

    def determine_tone(self, text):
        """Determine the tone of the response based on user input."""
        if re.search(r"please|thank you", text, re.IGNORECASE):
            return "formal"
        elif re.search(r"help|support|struggling", text, re.IGNORECASE):
            return "empathetic"
        else:
            return self.default_tone

    def generate_response(self, sentiment, tone, user_input):
        """Generate a response based on sentiment and tone."""
        response = random.choice(self.tone_adaptations.get(tone, self.default_responses))
        if tone == "empathetic" and sentiment == "negative":
            response += " I'm here to support you through this."
        elif tone == "friendly" and sentiment == "positive":
            response += " It's great to see you're feeling this way!"
        return response

    def log_interaction(self, user_input, sentiment, tone):
        """Log user interactions for future analysis."""
        self.interaction_history.append({
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "sentiment": sentiment,
            "tone": tone
        })

    def update_language_patterns(self, new_patterns):
        """Add new language patterns for better understanding."""
        self.known_patterns.update(new_patterns)
        print("Language patterns updated successfully.")

    def review_interactions(self):
        """Review logged interactions for patterns and improvement."""
        for interaction in self.interaction_history:
            print(interaction)


# Example Usage
if __name__ == "__main__":
    sidekick_language = LanguageModel()

    # Simulate user interaction
    user_input = input("You: ")
    sentiment, tone = sidekick_language.process_input(user_input)
    response = sidekick_language.generate_response(sentiment, tone, user_input)
    print(f"Sidekick: {response}")

    # Update language patterns
    new_patterns = {
        "greetings": ["hello", "hi", "good morning", "good evening"],
        "farewells": ["bye", "goodbye", "see you", "take care"]
    }
    sidekick_language.update_language_patterns(new_patterns)

    # Review interaction history
    sidekick_language.review_interactions()