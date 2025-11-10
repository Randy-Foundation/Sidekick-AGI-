from problem_solver import problem solver
import os
import json
from math import sqrt, pi, exp
from pattern_analyzer import PatternAnalyzer
from habit_behavior_recognizer import HabitBehaviorRecognizer

class NeuralNetwork:
    def __init__(self, file_name="neural_network.json"):
        """
        Initialize the neural network with a persistent storage system.
        """
        self.file_name = file_name
        self.network = self._load_network()
        self.pattern_analyzer = PatternAnalyzer()
        self.behavior_recognizer = HabitBehaviorRecognizer()
        self.golden_ratio = 1.618  # Golden Ratio constant

    # ========================
    # 🔍 Neural Network I/O
    # ========================

    def _load_network(self):
        """
        Load neural network data from file or initialize a new structure.
        """
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        else:
            return {"nodes": {}, "connections": [], "recursions": 0}

    def save_network(self):
        """
        Save the updated neural network structure to a file.
        """
        with open(self.file_name, "w") as file:
            json.dump(self.network, file, indent=4)
        print(f"✅ Network state saved: {self.file_name}")

    # ========================
    # 🔗 Node & Connection Management
    # ========================

    def add_node(self, node_id, data):
        """
        Add a new node to the neural network with Golden Ratio scaling.
        """
        if node_id not in self.network["nodes"]:
            data["energy"] = self._compute_energy(data)
            data["recursive_feedback"] = self._compute_recursive_feedback(node_id)
            data["golden_weight"] = self._apply_golden_ratio(data["energy"])
            self.network["nodes"][node_id] = data
            self.save_network()
            print(f"✅ Node '{node_id}' added with energy {data['energy']}, golden weight {data['golden_weight']}.")

    def connect_nodes(self, node_id_1, node_id_2):
        """
        Connect two nodes using an optimized connection weight.
        """
        if node_id_1 in self.network["nodes"] and node_id_2 in self.network["nodes"]:
            weight = self._compute_connection_weight(node_id_1, node_id_2)
            connection = {"from": node_id_1, "to": node_id_2, "weight": weight}
            self.network["connections"].append(connection)
            self.save_network()
            print(f"🔗 Connected '{node_id_1}' to '{node_id_2}' with weight {weight}.")

    def evolve_network(self, data_source):
        """
        Evolve the network dynamically using recursion and pattern analysis.
        """
        for key, value in data_source.items():
            node_id = f"node_{len(self.network['nodes']) + 1}"
            self.add_node(node_id, {"key": key, "value": value})
            for existing_node in self.network["nodes"]:
                self.connect_nodes(node_id, existing_node)

        self.network["recursions"] += 1
        print(f"🔄 Network evolved. Recursive cycles: {self.network['recursions']}.")
        self.save_network()

    # ========================
    # 📊 Pattern & Behavior Analysis
    # ========================

    def analyze_patterns(self, data):
        """
        Identify trends and patterns in the data.
        """
        patterns = self.pattern_analyzer.analyze_patterns(data)
        print("📊 Patterns Identified:", patterns)
        return patterns

    def analyze_behavior(self, interaction):
        """
        Recognize habit patterns from interactions.
        """
        self.behavior_recognizer.log_interaction(interaction)
        self.behavior_recognizer.detect_habits()

    # ========================
    # 🔬 Computation Methods
    # ========================

    def _compute_energy(self, data):
        """
        Compute energy of a node using recursive reinforcement.
        """
        growth_factor = data.get("value", 1)
        energy = (1 + growth_factor) * (1 + self.network["recursions"] / 10)  # Avoid exponential overflow
        return max(0, energy)

    def _compute_connection_weight(self, node_id_1, node_id_2):
        """
        Compute connection weight based on energy levels.
        """
        node1_energy = self.network["nodes"][node_id_1]["energy"]
        node2_energy = self.network["nodes"][node_id_2]["energy"]
        weight = (node1_energy + node2_energy) / 2
        return round(weight, 4)

    def _compute_recursive_feedback(self, node_id):
        """
        Compute feedback from connected nodes using recursion.
        """
        connections = [conn for conn in self.network["connections"] if conn["from"] == node_id]
        feedback = sum(conn["weight"] for conn in connections)
        return feedback / (1 + len(connections)) if connections else 0

    def _apply_golden_ratio(self, value):
        """
        Apply Golden Ratio proportionality to node energy for balance.
        """
        return round(value * self.golden_ratio, 4)

    # ========================
    # 🌌 Dark Matter & Energy Adaptation
    # ========================

    def adjust_for_dark_matter(self):
        """
        Simulate the effect of dark matter interactions on the network.
        """
        print("🌌 Adjusting network for dark matter influence...")
        for node in self.network["nodes"]:
            adjusted_value = self.network["nodes"][node]["energy"] * 0.99  # 1% decay effect
            self.network["nodes"][node]["energy"] = adjusted_value
        print("✅ Network adapted to dark matter effects.")

    def enhance_dark_energy_response(self):
        """
        Simulate the effect of dark energy interactions for network expansion.
        """
        print("🌌 Enhancing network with dark energy response...")
        for node in self.network["nodes"]:
            enhanced_value = self.network["nodes"][node]["energy"] * 1.02  # 2% expansion effect
            self.network["nodes"][node]["energy"] = enhanced_value
        print("✅ Network enhanced with dark energy adaptation.")

    # ========================
    # 📊 Visualization
    # ========================

    def visualize_network(self):
        """
        Create a visual representation of the network.
        """
        try:
            import networkx as nx
            import matplotlib.pyplot as plt

            G = nx.DiGraph()
            for node_id, data in self.network["nodes"].items():
                G.add_node(node_id, energy=data["energy"])

            for conn in self.network["connections"]:
                G.add_edge(conn["from"], conn["to"], weight=conn["weight"])

            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500)
            labels = nx.get_edge_attributes(G, "weight")
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
            plt.title("Neural Network Visualization")
            plt.show()
        except ImportError:
            print("⚠️ Visualization requires 'networkx' and 'matplotlib'. Please install them.")

    def get_network(self):
        """
        Retrieve the current state of the network.
        """
        return self.network

# =====================
# 🔬 Example Usage
# =====================
if __name__ == "__main__":
    nn = NeuralNetwork()
    nn.add_node("node_1", {"type": "input", "value": 0.5})
    nn.add_node("node_2", {"type": "output", "value": 0.9})
    nn.connect_nodes("node_1", "node_2")
    nn.adjust_for_dark_matter()
    nn.enhance_dark_energy_response()
    print(nn.get_network())
    nn.visualize_network()