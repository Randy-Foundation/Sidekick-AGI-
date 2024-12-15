class LanguageModel:
    def __init__(self):
        """Initialize the language model."""
        print("Language Model Initialized.")

    def analyze_command(self, command):
        """
        Analyze the input command and return an interpretation.
        """
        # Basic command recognition
        command = command.lower()
        if "check security" in command:
            return {"action": "check_security"}
        elif "list devices" in command:
            return {"action": "list_devices"}
        elif "approve device" in command:
            device_name = command.split("approve device")[-1].strip()
            return {"action": "approve_device", "device_name": device_name}
        elif "revoke device" in command:
            device_name = command.split("revoke device")[-1].strip()
            return {"action": "revoke_device", "device_name": device_name}
        elif "add cloud" in command:
            service_name = command.split("add cloud")[-1].strip()
            return {"action": "add_cloud", "service_name": service_name}
        elif "remove cloud" in command:
            service_name = command.split("remove cloud")[-1].strip()
            return {"action": "remove_cloud", "service_name": service_name}
        elif "log activity" in command:
            activity = command.split("log activity")[-1].strip()
            return {"action": "log_activity", "activity": activity}
        elif "show logs" in command:
            return {"action": "show_logs"}
        elif "analyze habits" in command:
            return {"action": "analyze_habits"}
        elif "exit" in command:
            return {"action": "exit"}
        else:
            return {"action": "unknown", "message": "Command not recognized. Please try again."}

# Example usage
if __name__ == "__main__":
    lm = LanguageModel()
    print(lm.analyze_command("approve device Laptop"))