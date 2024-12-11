import os
from data_handler import DataHandler
from neural_network import NeuralNetwork

class SidekickUI:
    def __init__(self, creator_passphrase="randell_master"):
        self.data_handler = DataHandler()
        self.neural_network = NeuralNetwork()
        self.creator_passphrase = creator_passphrase

    def start(self):
        """
        Main conversational loop.
        """
        print("Hello! I'm Sidekick, your personal AI companion.")
        print("How can I assist you today?")
        while True:
            user_input = input("You: ").strip().lower()

            if user_input in ["exit", "quit"]:
                print("Goodbye! Remember, I'm always here to help.")
                break
            elif user_input == "self-update":
                self.self_update()
            elif user_input == "manual-update":
                self.manual_update()
            elif user_input == "view network":
                print(self.neural_network.get_network())
            elif user_input == "help":
                print("Commands: 'self-update', 'manual-update', 'view network', 'help', 'exit'")
            else:
                print("I didn’t understand that. Try 'help' for options.")

    def self_update(self):
        """
        Sidekick creates or modifies files autonomously for self-improvement.
        """
        next_file_name = f"self_update_{len(self.neural_network.network['nodes']) + 1}.py"
        file_content = self.generate_update_code()

        with open(next_file_name, "w") as file:
            file.write(file_content)

        print(f"Sidekick has created a new self-update file: {next_file_name}")

    def manual_update(self):
        """
        Allow the creator to add or modify code directly.
        """
        passphrase = input("Enter the creator passphrase: ").strip()
        if passphrase != self.creator_passphrase:
            print("Access denied. Only the creator can perform this action.")
            return

        file_name = input("Enter the file name to create/update (e.g., 'new_file.py'): ").strip()
        content = input("Enter the content to write to the file: ")

        with open(file_name, "w") as file:
            file.write(content)

        print(f"File '{file_name}' has been created/updated by the creator.")

    def generate_update_code(self):
        """
        Generate code for Sidekick's self-evolution.
        """
        return f"""
# Auto-generated file by Sidekick for self-evolution
from neural_network import NeuralNetwork

class SelfUpdate:
    def __init__(self):
        self.neural_network = NeuralNetwork()

    def enhance(self):
        # Example: Add a new node and connect it
        node_id = "auto_node_{len(self.neural_network.network['nodes']) + 1}"
        self.neural_network.add_node(node_id, {{"type": "auto-generated", "purpose": "evolution"}})
        for existing_node in self.neural_network.network['nodes']:
            self.neural_network.connect_nodes(node_id, existing_node)

# Execute the enhancement
if __name__ == "__main__":
    updater = SelfUpdate()
    updater.enhance()
"""

# Example usage
if __name__ == "__main__":
    ui = SidekickUI()
    ui.start()