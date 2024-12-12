from network_manager import NetworkManager
from data_handler import DataHandler
from security import SimpleSecurity
from belief_system import BeliefSystem

class Sidekick:
    def __init__(self, creator_id):
        """Initialize Sidekick with all core modules."""
        self.creator_id = creator_id
        self.data_handler = DataHandler()
        self.network_manager = NetworkManager(creator_id=creator_id)
        self.security = SimpleSecurity(key="your-secret-key")
        self.belief_system = BeliefSystem()
        self.network_manager.log_event("Sidekick initialized with networking and belief system capabilities.")

    def interact(self):
        """Main interaction loop."""
        print("Hello, I'm Sidekick. How can I assist you today?")
        while True:
            user_input = input("> ").strip().lower()
            if user_input == "exit":
                print("Goodbye! Talk to you later.")
                break
            elif user_input.startswith("network"):
                self.handle_network_commands(user_input)
            elif user_input.startswith("security"):
                self.handle_security_commands(user_input)
            elif user_input.startswith("belief"):
                self.handle_belief_commands(user_input)
            else:
                print("I didn’t understand that. Can you rephrase?")

    def handle_network_commands(self, command):
        """Process network-related commands."""
        if "discover" in command:
            devices = self.network_manager.discover_devices()
            print("Devices discovered:")
            for device in devices:
                print(f"- {device['name']} ({device['ip']})")
        elif "approve" in command:
            device_name = input("Enter device name: ")
            ip_address = input("Enter device IP address: ")
            self.network_manager.approve_device(device_name, ip_address)
        elif "suggest security" in command:
            self.network_manager.suggest_security_measures()
        elif "sync cloud" in command:
            service_name = input("Enter cloud service name: ")
            self.network_manager.sync_with_cloud(service_name)
        else:
            print("Network command not recognized.")

    def handle_security_commands(self, command):
        """Process security-related commands."""
        if "encrypt" in command:
            sensitive_data = input("Enter data to encrypt: ")
            encrypted = self.security.encrypt_data(sensitive_data)
            print(f"Encrypted data: {encrypted}")
        elif "decrypt" in command:
            encrypted_data = input("Enter data to decrypt: ")
            try:
                decrypted = self.security.decrypt_data(encrypted_data)
                print(f"Decrypted data: {decrypted}")
            except Exception as e:
                print(f"Error decrypting data: {e}")
        else:
            print("Security command not recognized.")

    def handle_belief_commands(self, command):
        """Process belief system-related commands."""
        if "profile" in command:
            belief_profile = self.belief_system.get_belief_profile()
            print("Current Belief Profile:")
            for key, value in belief_profile.items():
                print(f"{key}: {value}")
        elif "update" in command:
            belief_update = input("Enter belief update data: ")
            self.belief_system.update_beliefs(belief_update)
            print("Belief system updated.")
        else:
            print("Belief command not recognized.")

# Example usage
if __name__ == "__main__":
    sidekick = Sidekick(creator_id="your_creator_id")
    sidekick.interact()