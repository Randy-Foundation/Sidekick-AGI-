from network_manager import NetworkManager
from command_manager import CommandManager

class SidekickUI:
    def __init__(self):
        """
        Initialize the Sidekick UI with essential components,
        including the network manager, command manager, and creator ID.
        """
        self.creator_id = "Randell_Murrin"
        self.network_manager = NetworkManager(creator_id=self.creator_id)
        self.command_manager = CommandManager()

    def start(self):
        """Start the Sidekick user interface."""
        print("Welcome to Sidekick!")
        print("Type 'help' to see available commands or 'exit' to stop.")
        
        # Example interaction at startup
        self.network_manager.approve_device("Smartphone", self.creator_id)
        self.network_manager.log_network_activity("Smartphone connected to network.")
        self.network_manager.check_security()

        # Interactive loop to receive user commands
        self.interactive_loop()

    def interactive_loop(self):
        """Continuous loop to process user commands."""
        while True:
            user_input = input("\nEnter a command: ")
            if user_input.lower() == "exit":
                print("Goodbye! Sidekick shutting down.")
                break
            elif user_input.lower() == "help":
                self.display_help()
            else:
                self.command_manager.execute_command(user_input)

    def display_help(self):
        """Display a list of available commands."""
        print("\nAvailable Commands:")
        print("- 'log behavior': Detect user habits and behaviors.")
        print("- 'check network': Perform a network security check.")
        print("- 'show beliefs': Display Sidekick's belief system.")
        print("- 'log activity <description>': Log a specific activity.")
        print("- 'exit': Exit the program.")

# Example usage
if __name__ == "__main__":
    ui = SidekickUI()
    ui.start()