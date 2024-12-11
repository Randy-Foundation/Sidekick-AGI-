import os
import json
import random

class NeuralNetwork:
    def __init__(self, file_name="neural_network.json"):
        """
        Initialize the neural network with a file for persistent storage.
        """
        self.file_name = file_name
        self.network = self._load_network()

    def _load_network(self):
        """
        Load the neural network data from a file, or create a new structure if none exists.
        """
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        else:
            return {"nodes": {}, "connections": []}

    def save_network(self):
        """
        Save the current neural network structure to a file.
        """
        with open(self.file_name, "w") as file:
            json.dump(self.network, file, indent=4)

    def add_node(self, node_id, data):
        """
        Add a new node to the neural network.
        """
        if node_id not in self.network["nodes"]:
            self.network["nodes"][node_id] = data
            self.save_network()

    def connect_nodes(self, node_id_1, node_id_2, weight=None):
        """
        Connect two nodes in the neural network with an optional weight.
        """
        if node_id_1 in self.network["nodes"] and node_id_2 in self.network["nodes"]:
            connection = {
                "from": node_id_1,
                "to": node_id_2,
                "weight": weight if weight is not None else random.uniform(-1, 1),
            }
            self.network["connections"].append(connection)
            self.save_network()

    def evolve_network(self, data_source):
        """
        Use a data source to generate new nodes and connections.
        """
        for key, value in data_source.items():
            node_id = f"node_{len(self.network['nodes']) + 1}"
            self.add_node(node_id, {"key": key, "value": value})
            for existing_node in self.network["nodes"]:
                self.connect_nodes(node_id, existing_node)

    def get_network(self):
        """
        Retrieve the current state of the neural network.
        """
        return self.network

# Example usage:
# nn = NeuralNetwork()
# nn.add_node("node_1", {"type": "input", "value": "Hello"})
# nn.add_node("node_2", {"type": "output", "value": "Hi there!"})
# nn.connect_nodes("node_1", "node_2")
# print(nn.get_network())