import datetime

class HabitBehaviorRecognizer:
    """
    Recognize and analyze user habits and behavioral patterns.
    """

    def __init__(self):
        self.habits = {}
        self.behavior_logs = []

    def log_behavior(self, behavior_type, details):
        """
        Log user behavior with a timestamp.
        """
        timestamp = datetime.datetime.now()
        log_entry = {"type": behavior_type, "details": details, "timestamp": timestamp}
        self.behavior_logs.append(log_entry)
        print(f"Logged behavior: {behavior_type} at {timestamp}")

    def analyze_patterns(self):
        """
        Analyze behavior logs to identify patterns.
        """
        print("\nAnalyzing behavior patterns...")
        pattern_summary = {}
        for log in self.behavior_logs:
            behavior_type = log["type"]
            if behavior_type not in pattern_summary:
                pattern_summary[behavior_type] = 0
            pattern_summary[behavior_type] += 1

        for behavior, count in pattern_summary.items():
            print(f"Behavior: {behavior} | Count: {count}")
        return pattern_summary

    def detect_habits(self):
        """
        Identify recurring behaviors as habits.
        """
        print("\nDetecting recurring habits...")
        patterns = self.analyze_patterns()
        for behavior, count in patterns.items():
            if count >= 3:  # Threshold for habit detection
                self.habits[behavior] = count
        print(f"Identified habits: {self.habits}")
        return self.habits

    def suggest_improvements(self):
        """
        Suggest improvements based on detected habits.
        """
        print("\nSuggesting improvements...")
        for habit, count in self.habits.items():
            if habit.lower() == "excessive screen time":
                print("Suggestion: Take breaks and limit screen usage.")
            elif habit.lower() == "late-night browsing":
                print("Suggestion: Set a bedtime routine for better sleep.")
            else:
                print(f"Suggestion: Monitor and evaluate habit '{habit}' for improvement.")

# Example usage
if __name__ == "__main__":
    recognizer = HabitBehaviorRecognizer()
    recognizer.log_behavior("Excessive Screen Time", "Used phone for 4 hours")
    recognizer.log_behavior("Excessive Screen Time", "Used phone for 3 hours")
    recognizer.log_behavior("Late-night Browsing", "Browsing the web at 1 AM")
    recognizer.log_behavior("Excessive Screen Time", "Used phone for 5 hours")

    recognizer.detect_habits()
    recognizer.suggest_improvements()