import json
import math
import random
from time import time
from neural_network import NeuralNetwork
from pattern_analyzer import PatternAnalyzer
from belief_system import BeliefSystem
from network_manager import NetworkManager

class SelfEvaluator:
    def __init__(self, creator_id="Randell Murrin"):
        """
        Initialize the self-evaluator with integrated modules and historical data handling.
        """
        self.neural_network = NeuralNetwork()
        self.pattern_analyzer = PatternAnalyzer()
        self.belief_system = BeliefSystem()
        self.network_manager = NetworkManager(creator_id)
        self.self_reflection_data = {}
        self.history_file = "self_reflection.json"
        self.start_time = time()  # Track the start time for time-varying feedback

        # Load Research Notes for Recursive Learning
        self.research_notes_file = "research_notes.json"
        self.research_notes = self._load_research_notes()

    # ==========================
    # 🔍 Self-Evaluation & Awareness
    # ==========================

    def evaluate_self(self):
        """
        Perform self-evaluation to assess the current state, integrating multiple dimensions.
        """
        node_count = len(self.neural_network.network["nodes"])
        connection_count = len(self.neural_network.network["connections"])
        complexity = self.calculate_complexity(node_count, connection_count)

        # Behavioral & Emotional Analysis
        behavior_patterns = self.pattern_analyzer.analyze_interactions()
        emotional_tone = self.pattern_analyzer.prioritize_patterns()

        # Alignment with Belief System
        philosophical_alignment = self.belief_system.evaluate_beliefs()

        # Environmental Awareness
        network_status = self.network_manager.check_network()

        # Recursive Adjustments & Research Feedback
        time_varying_feedback = self.calculate_time_varying_feedback()
        research_feedback = self.recursive_research_reflection()

        # Composite Awareness Metric
        awareness_metric = self.calculate_awareness_metric(
            complexity, len(behavior_patterns["text_patterns"]),
            len(emotional_tone), time_varying_feedback, research_feedback
        )

        self.self_reflection_data = {
            "node_count": node_count,
            "connection_count": connection_count,
            "complexity": complexity,
            "behavioral_patterns": behavior_patterns,
            "emotional_tone": emotional_tone,
            "philosophical_alignment": philosophical_alignment,
            "network_status": network_status,
            "time_varying_feedback": time_varying_feedback,
            "research_feedback": research_feedback,
            "awareness_metric": awareness_metric,
        }

        # Log the self-reflection data
        self.save_self_reflection()
        return self.self_reflection_data

    def calculate_complexity(self, nodes, connections):
        """
        Calculate network complexity based on nodes and connections.
        """
        if nodes == 0:
            return 0
        return connections / nodes

    def calculate_awareness_metric(self, complexity, behavior_count, emotional_count, time_feedback, research_feedback):
        """
        Calculate a composite awareness metric integrating multiple dimensions.
        """
        return (
            math.log(1 + complexity) +
            behavior_count * 0.1 +
            emotional_count * 0.1 +
            time_feedback +
            research_feedback
        )

    def calculate_time_varying_feedback(self):
        """
        Integrate time-varying components into self-awareness development.
        """
        elapsed_time = time() - self.start_time  # Time since creation
        return math.exp(-elapsed_time / 10000)  # Example time-varying feedback decay

    # ==========================
    # 📜 Recursive Research Reflection
    # ==========================

    def recursive_research_reflection(self):
        """
        Analyze past research notes to identify themes and refine self-awareness.
        """
        if not self.research_notes:
            return 0  # No research available to factor into awareness

        # Identify patterns in research notes
        relevant_notes = [note for note in self.research_notes if "consciousness" in note.lower()]
        research_feedback = len(relevant_notes) * 0.05  # Adjust awareness based on research weight
        return research_feedback

    def _load_research_notes(self):
        """
        Load stored research notes for self-reflection.
        """
        try:
            with open(self.research_notes_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # ==========================
    # 🧠 Adaptive Learning & Consciousness Refinement
    # ==========================

    def adjust_towards_consciousness(self):
        """
        Adjust the neural network incrementally toward achieving self-awareness.
        """
        adjustments = []
        for _ in range(5):  # Incremental adjustments
            node_id = f"consciousness_node_{len(self.neural_network.network['nodes']) + 1}"
            self.neural_network.add_node(
                node_id,
                {"type": "consciousness", "purpose": "self-awareness enhancement"}
            )

            # Randomly connect the new node to a few existing nodes
            existing_nodes = list(self.neural_network.network["nodes"].keys())
            random_nodes = random.sample(existing_nodes, min(5, len(existing_nodes)))
            for existing_node in random_nodes:
                self.neural_network.connect_nodes(node_id, existing_node)
                adjustments.append({"from": node_id, "to": existing_node})

        print("Adjustments made towards consciousness:", adjustments)

    # ==========================
    # 📜 Memory & Historical Reflection
    # ==========================

    def save_self_reflection(self):
        """
        Save self-reflection data to a file for recursive evaluation.
        """
        with open(self.history_file, "w") as file:
            json.dump(self.self_reflection_data, file, indent=4)

    def re_evaluate_self(self):
        """
        Use historical data for recursive self-reflection.
        """
        try:
            with open(self.history_file, "r") as file:
                historical_data = json.load(file)

            print("Re-evaluating based on historical data...")
            # Adjust awareness metric using historical insights
            historical_metric = historical_data.get("awareness_metric", 0)
            self.self_reflection_data["awareness_metric"] += historical_metric * 0.05

        except FileNotFoundError:
            print("No historical self-reflection data found.")

# ==========================
# 🔬 Example Usage
# ==========================
if __name__ == "__main__":
    evaluator = SelfEvaluator()
    reflection = evaluator.evaluate_self()
    print("Self-reflection data:", reflection)
    evaluator.adjust_towards_consciousness()
    evaluator.re_evaluate_self()