import datetime
from pattern_analyzer import PatternAnalyzer
from language_model import LanguageModel

class HabitBehaviorRecognizer:
    def __init__(self):
        """Initialize the habit and behavior recognizer."""
        self.user_patterns = {}  # Store identified patterns
        self.daily_logs = []  # Log daily interactions
        self.language_model = LanguageModel()
        self.pattern_analyzer = PatternAnalyzer()

    def log_interaction(self, interaction):
        """Log user interaction for analysis."""
        timestamp = datetime.datetime.now()
        tone = self.language_model.analyze_tone(interaction)
        log_entry = {
            "timestamp": timestamp,
            "interaction": interaction,
            "tone": tone,
        }
        self.daily_logs.append(log_entry)
        print(f"Logged interaction: '{interaction}' with tone: {tone} at {timestamp}")

    def detect_habits(self):
        """Analyze logs to identify habits and behavior patterns."""
        if not self.daily_logs:
            print("No interactions logged yet.")
            return
        
        print("Analyzing user habits...")
        patterns = self.pattern_analyzer.analyze_patterns(self.daily_logs)
        self.user_patterns = patterns
        for habit, details in patterns.items():
            print(f"Detected habit: {habit} - Frequency: {details['frequency']} - Tone: {details['tone']}")

    def suggest_improvements(self):
        """Provide insights or suggestions based on identified habits."""
        if not self.user_patterns:
            print("No habits detected yet.")
            return

        print("Suggestions for improvement based on your habits:")
        for habit, details in self.user_patterns.items():
            if details["frequency"] > 5:
                print(f"- Consider balancing your time spent on: {habit}")
            if "negative" in details["tone"]:
                print(f"- Habit '{habit}' seems to evoke negative emotions. Would you like assistance in addressing this?")

    def adjust_behavior_analysis(self):
        """Refine behavior analysis based on user feedback."""
        feedback = input("Have my insights been helpful? (yes/no): ").strip().lower()
        if feedback == "yes":
            print("Great! I'll continue improving.")
        else:
            print("Noted. I'll analyze and adjust my approach.")

    def respond_to_emotional_state(self, interaction):
        """Provide responses tailored to emotional state."""
        tone = self.language_model.analyze_tone(interaction)
        if tone == "positive":
            print("I'm glad you're feeling positive! Let's build on this energy.")
        elif tone == "negative":
            print("I'm here for you. Do you want to talk about what's bothering you?")
        else:
            print("Thanks for sharing your thoughts. Let me know how I can assist.")

    def save_patterns(self):
        """Save identified patterns for future reference."""
        try:
            with open("user_patterns.json", "w") as file:
                json.dump(self.user_patterns, file)
            print("Patterns saved successfully.")
        except Exception as e:
            print(f"Error saving patterns: {e}")

    def load_patterns(self):
        """Load previously identified patterns."""
        try:
            with open("user_patterns.json", "r") as file:
                self.user_patterns = json.load(file)
            print("Patterns loaded successfully.")
        except FileNotFoundError:
            print("No saved patterns found.")
        except Exception as e:
            print(f"Error loading patterns: {e}")

# Example Usage
if __name__ == "__main__":
    recognizer = HabitBehaviorRecognizer()
    recognizer.log_interaction("I had a productive day at work.")
    recognizer.log_interaction("I feel tired after my meeting.")
    recognizer.detect_habits()
    recognizer.suggest_improvements()
    recognizer.respond_to_emotional_state("I am feeling overwhelmed today.")