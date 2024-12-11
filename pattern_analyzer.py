from data_handler import DataHandler
from collections import Counter
from textblob import TextBlob  # For sentiment analysis


class PatternAnalyzer:
    def __init__(self):
        self.data_handler = DataHandler()

    def analyze_interactions(self):
        """
        Analyze interactions to find recurring patterns and emotional tones.
        """
        interactions = self.data_handler.get_all_data()["interactions"]
        if not interactions:
            return "No interactions to analyze."

        user_inputs = [interaction["user_input"] for interaction in interactions if "user_input" in interaction]
        emotional_analysis = [self.analyze_emotion(input_text) for input_text in user_inputs]

        # Count common patterns
        common_patterns = Counter(user_inputs).most_common()

        # Save identified patterns
        for pattern, count in common_patterns:
            if count > 1:  # Save patterns that occur more than once
                self.data_handler.add_pattern(
                    pattern,
                    {"count": count, "average_sentiment": self.average_emotion(emotional_analysis, pattern)}
                )

        return {"patterns": common_patterns, "emotional_analysis": emotional_analysis}

    def analyze_emotion(self, text):
        """
        Perform sentiment analysis on a given text to infer emotional tone.
        """
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity  # Range from -1 (negative) to 1 (positive)
        return {"text": text, "sentiment": sentiment}

    def average_emotion(self, emotional_data, pattern):
        """
        Calculate the average sentiment for a given pattern.
        """
        sentiments = [data["sentiment"] for data in emotional_data if pattern in data["text"]]
        return sum(sentiments) / len(sentiments) if sentiments else 0.0


# Example usage:
# analyzer = PatternAnalyzer()
# print(analyzer.analyze_interactions())