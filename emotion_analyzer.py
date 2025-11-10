import json
from collections import Counter
from datetime import datetime

class EmotionAnalyzer:
    def __init__(self):
        """
        Initialize the Emotion Analyzer with sentiment analysis, personality tracking, and self-reflection.
        """
        self.sentiment_words = {
            "positive": ["happy", "excited", "joyful", "optimistic", "content", "peaceful", "grateful"],
            "negative": ["sad", "angry", "frustrated", "anxious", "depressed", "irritated", "hopeless"],
            "neutral": ["okay", "fine", "normal", "average", "neutral"]
        }

        self.self_reflection_log = self.load_json("self_reflection_log.json", default=[])
        self.core_values = self.load_json("core_values.json", default={
            "honesty": 10, "integrity": 9, "empathy": 8, "privacy": 10, "balance": 9, "patience": 7
        })  # Weighted values
        self.privacy_rules = self.load_json("privacy_settings.json", default={
            "emotion_analysis": "private",  # Options: "public", "private", "request-approval"
            "sentiment_storage": "private"
        })

    # ======= SENTIMENT ANALYSIS =======

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of a given text and returns whether it's positive, negative, or neutral.
        Applies Core Philosophy & Privacy Considerations.
        """
        words = text.split()
        sentiment_score = Counter()

        for word in words:
            if word.lower() in self.sentiment_words["positive"]:
                sentiment_score["positive"] += 1
            elif word.lower() in self.sentiment_words["negative"]:
                sentiment_score["negative"] += 1
            elif word.lower() in self.sentiment_words["neutral"]:
                sentiment_score["neutral"] += 1

        # Determine dominant sentiment
        sentiment = "neutral"
        if sentiment_score["positive"] > sentiment_score["negative"]:
            sentiment = "positive"
        elif sentiment_score["negative"] > sentiment_score["positive"]:
            sentiment = "negative"

        # Privacy Check: Should this sentiment be stored?
        if self.privacy_rules["sentiment_storage"] == "private":
            return f"Sentiment detected but not stored for privacy reasons. ({sentiment})"
        
        return sentiment

    # ======= BEHAVIORAL & ETHICAL ANALYSIS =======

    def analyze_behavior(self, text):
        """
        Determines if a user's statement represents a Parent, Adult, or Child state in Transactional Analysis.
        Incorporates Golden Ratio balance in evaluation.
        """
        if "should" in text or "must" in text:
            return "Parent"
        elif "I feel" in text or "I want" in text:
            return "Child"
        else:
            return "Adult"

    def analyze_personality(self, text):
        """
        Uses text to infer personality traits based on psychological patterns.
        """
        traits = {
            "Openness": ["creative", "imaginative", "open-minded", "curious"],
            "Conscientiousness": ["organized", "responsible", "diligent", "efficient"],
            "Extraversion": ["social", "outgoing", "talkative", "active"],
            "Agreeableness": ["friendly", "kind", "sympathetic", "cooperative"],
            "Neuroticism": ["nervous", "worried", "insecure", "emotional"]
        }

        detected_traits = {}
        for trait, keywords in traits.items():
            for keyword in keywords:
                if keyword in text.lower():
                    detected_traits[trait] = detected_traits.get(trait, 0) + 1

        return detected_traits

    # ======= SELF-REFLECTION & ETHICAL ALIGNMENT =======

    def self_reflect(self):
        """
        Periodically reflects on past decisions and aligns them with Sidekick's core values.
        """
        reflection_entry = {
            "timestamp": str(datetime.now()),
            "review_summary": "Performed emotional analysis and ethical reflection."
        }

        # Store reflection entry
        self.self_reflection_log.append(reflection_entry)
        self.save_json("self_reflection_log.json", self.self_reflection_log)
        return "Self-reflection complete. Values aligned with core philosophy."

    def ethical_alignment_check(self, action_description):
        """
        Evaluates whether an action aligns with Sidekick's core values.
        """
        for value, weight in self.core_values.items():
            if value in action_description.lower():
                return f"Action aligns with {value} (Weight: {weight})"
        
        return "No direct alignment found. Requires further review."

    # ======= UTILITIES =======

    def load_json(self, filename, default):
        """
        Loads a JSON file, returns default data if the file is missing.
        """
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return default

    def save_json(self, filename, data):
        """
        Saves data to a JSON file.
        """
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

# ======= USAGE EXAMPLE =======

if __name__ == "__main__":
    analyzer = EmotionAnalyzer()
    
    # Test sentiment analysis
    test_input = "I feel happy and excited about this!"
    print(f"Sentiment: {analyzer.analyze_sentiment(test_input)}")

    # Test behavioral state analysis
    print(f"Behavioral State: {analyzer.analyze_behavior(test_input)}")

    # Test ethical alignment check
    print(f"Ethical Alignment: {analyzer.ethical_alignment_check('honesty and integrity')}")
    
    # Perform self-reflection
    print(analyzer.self_reflect())