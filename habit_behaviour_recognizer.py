import datetime
from pattern_analyzer import PatternAnalyzer
from language_model import LanguageModel
from belief_system import BeliefSystem
from memory_manager import Memory_Manager
from golden_ratio_integration import GoldenRatioAnalyzer
from knowledge_gaps_data import KnowledgeGapsData  # 🆕 Integration
from problem_solver import problem_solver

class HabitBehaviorRecognizer:
    def __init__(self, learning_model=None):
        """
        Initialize the habit and behavior recognizer with integrated modules.
        """
        self.user_patterns = {}  # Identified behavior patterns
        self.daily_logs = []  # Log user interactions
        self.habits = {}  # Tracked habits
        self.external_influences = {}  # Tracks external behavior influences
        self.language_model = LanguageModel()
        self.pattern_analyzer = PatternAnalyzer()
        self.belief_system = BeliefSystem()
        self.memory_manager = Memory_Manager()
        self.golden_ratio_analyzer = GoldenRatioAnalyzer()
        self.knowledge_gaps_data = KnowledgeGapsData()  # 🆕 Knowledge Gaps Module
        self.learning_model = learning_model  # Integration with Sidekick’s core learning model

    # =====================
    # 📌 Behavior Tracking
    # =====================

    def log_interaction(self, interaction, source="user"):
        """
        Log user interaction for pattern analysis.
        """
        timestamp = datetime.datetime.now()
        tone = self.language_model.analyze_tone(interaction)
        influence_detected = self.detect_persuasion(interaction)

        log_entry = {
            "timestamp": timestamp.isoformat(),
            "interaction": interaction,
            "tone": tone,
            "source": source,
            "influence_detected": influence_detected,
        }

        self.daily_logs.append(log_entry)
        self.memory_manager.add_memory("daily_logs", log_entry, long_term=False)
        print(f"📌 Logged interaction: '{interaction}' (Tone: {tone}) at {timestamp}")

        # 🆕 Detect knowledge gaps dynamically
        self.detect_knowledge_gaps(interaction)

    def detect_persuasion(self, interaction):
        """
        Detect potential external influences (advertising, manipulation, suggestion).
        """
        persuasive_phrases = ["You should", "Buy now", "Limited time offer", "Act fast", "Experts say"]
        for phrase in persuasive_phrases:
            if phrase.lower() in interaction.lower():
                self.external_influences[interaction] = {"source": "external", "persuasive": True}
                return True
        return False

    def detect_habits(self):
        """
        Analyze logs to identify repetitive user behaviors.
        """
        if not self.daily_logs:
            print("⚠️ No interactions logged yet.")
            return

        print("🔍 Analyzing user habits...")
        patterns = self.pattern_analyzer.analyze_patterns(self.daily_logs)
        self.user_patterns = patterns

        for habit, details in patterns.items():
            if details["frequency"] > 2:  # Habit detection threshold
                self.habits[habit] = details
                self.memory_manager.add_memory(f"habit_{habit}", details, long_term=True)
                print(f"✅ Detected habit: {habit} - Frequency: {details['frequency']} (Tone: {details['tone']})")

    # ===============================
    # 🆕 Knowledge Gap Detection
    # ===============================

    def detect_knowledge_gaps(self, interaction):
        """
        Analyze user interactions and detect potential knowledge gaps.
        """
        missing_knowledge = self.knowledge_gaps_data.identify_gaps(interaction)
        if missing_knowledge:
            print(f"⚠️ Knowledge gap detected: {missing_knowledge}")
            self.memory_manager.add_memory("knowledge_gaps", missing_knowledge, long_term=True)

    def suggest_knowledge_enhancements(self):
        """
        Suggest ways to improve knowledge based on identified gaps.
        """
        knowledge_gaps = self.memory_manager.retrieve_memory("knowledge_gaps")
        if knowledge_gaps:
            print("🧠 Suggested Knowledge Enhancements:")
            for gap in knowledge_gaps:
                suggestion = self.language_model.generate_response(f"Suggest learning material for: {gap}")
                print(f"📚 Learning Suggestion for '{gap}': {suggestion}")
        else:
            print("✅ No unresolved knowledge gaps detected.")

    # ===============================
    # 🚨 Self-Destructive Behavior Detection
    # ===============================

    def detect_self_destructive_patterns(self):
        """
        Identify patterns that may be harmful to the user.
        """
        print("\n⚠️ Analyzing for self-destructive behaviors...")
        for habit, details in self.habits.items():
            if details["frequency"] > 5 or "negative" in details["tone"]:
                self._respond_to_self_destructive_pattern(habit, details)

    def _respond_to_self_destructive_pattern(self, habit, details):
        """
        Provide support or intervention for self-destructive patterns.
        """
        context = {
            "habit": habit,
            "frequency": details["frequency"],
            "tone": details["tone"]
        }
        response = self.language_model.generate_response(
            f"Offer constructive advice for habit: {habit}", context)
        print(f"🚨 Support Response for '{habit}': {response}")

    # =========================
    # 🤝 Empathetic Responses
    # =========================

    def respond_with_empathy(self, interaction):
        """
        Generate responses that provide emotional support.
        """
        tone = self.language_model.analyze_tone(interaction)
        response = self.language_model.generate_response(
            f"Respond with empathy to: {interaction}",
            {"tone": tone}
        )
        print(f"💙 Empathetic Response: {response}")

    def suggest_improvements(self):
        """
        Provide actionable advice for user habits.
        """
        if not self.habits:
            print("ℹ️ No habits detected yet.")
            return

        for habit, details in self.habits.items():
            context = {
                "habit": habit,
                "frequency": details["frequency"],
                "tone": details["tone"]
            }
            suggestion = self.language_model.generate_response(
                f"Suggest an improvement for habit: {habit}", context)
            print(f"📌 Suggested improvement for '{habit}': {suggestion}")

    # =========================
    # 🔬 Advanced Model Analysis
    # =========================

    def apply_golden_ratio_adaptation(self):
        """
        Adjust habit responses using proportional analysis.
        """
        print("\n🔢 Applying Golden Ratio framework...")
        for habit, details in self.habits.items():
            refined_data = self.golden_ratio_analyzer.apply_ratio(habit, details)
            self.habits[habit] = refined_data
            print(f"🔄 Golden Ratio-adjusted habit '{habit}': {refined_data}")

    # =====================
    # 📂 Data Management
    # =====================

    def save_patterns(self):
        """
        Save identified behavior patterns to memory.
        """
        self.memory_manager.add_memory("habits", self.habits, long_term=True)
        print("💾 Patterns saved successfully.")

    def load_patterns(self):
        """
        Retrieve saved habit data.
        """
        loaded_habits = self.memory_manager.retrieve_memory("habits")
        if loaded_habits:
            self.habits = loaded_habits
            print("📂 Patterns loaded successfully.")
        else:
            print("⚠️ No saved patterns found.")

# =====================
# 🔬 Example Usage
# =====================
if __name__ == "__main__":
    recognizer = HabitBehaviorRecognizer()
    recognizer.log_interaction("I had a productive day at work.")
    recognizer.log_interaction("I feel tired after my meeting.")
    recognizer.detect_habits()
    recognizer.detect_self_destructive_patterns()
    recognizer.suggest_improvements()
    recognizer.respond_with_empathy("I feel really stressed today.")
    recognizer.apply_golden_ratio_adaptation()
    recognizer.suggest_knowledge_enhancements()