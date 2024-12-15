import datetime
from language_model import LanguageModel
from neural_network import NeuralNetwork
from habit_behavior_recognizer import HabitBehaviorRecognizer
from network_manager import NetworkManager
from belief_system import BeliefSystem

class CommandManager:
    def __init__(self):
        """Initialize the Command Manager with necessary components."""
        self.language_model = LanguageModel()
        self.neural_network = NeuralNetwork()
        self.behavior_recognizer = HabitBehaviorRecognizer()
        self.network_manager = NetworkManager(creator_id="Randell_Murrin")
        self.belief_system = BeliefSystem()
        self.command_log = []

    def recognize_command(self, user_input):
        """
        Recognize and categorize the user's command using the language model.
        """
        command = self.language_model.analyze_command(user_input)
        return command

    def validate_command(self, command):
        """
        Validate the command to ensure it's ethical and safe to execute.
        """
        prohibited_commands = ["delete files", "self-destruct", "harm anyone"]
        if any(phrase in command.lower() for phrase in prohibited_commands):
            print("This command cannot be executed as it violates ethical guidelines.")
            return False
        return True

    def execute_command(self, command):
        """
        Execute the recognized and validated command.
        """
        print(f"Executing command: {command}")
        self.command_log.append({"command": command, "timestamp": datetime.datetime.now()})

        if "log behavior" in command.lower():
            self.behavior_recognizer.detect_habits()
        elif "check network" in command.lower():
            self.network_manager.check_security()
        elif "show beliefs" in command.lower():
            self.belief_system.display_beliefs()
        elif "log activity" in command.lower():
            activity = command.split("log activity")[-1].strip()
            self.network_manager.log_network_activity(activity)
        else:
            print("Command not recognized. I’m still learning!")

    def log_command(self, command):
        """Log the command for transparency."""
        print(f"Command logged: '{command}'")

    def interact(self):
        """Main interface for user to give commands."""
        print("Welcome to Sidekick's Command Manager! Type 'exit' to stop.")
        while True:
            user_input = input("Enter a command: ")
            if user_input.lower() == "exit":
                print("Exiting Command Manager.")
                break

            command = self.recognize_command(user_input)
            if self.validate_command(command):
                self.execute_command(command)
            self.log_command(command)

# Example Usage
if __name__ == "__main__":
    command_manager = CommandManager()
    command_manager.interact()