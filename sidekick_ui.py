import sys
import os
import traceback
import datetime
import json
import logging

# Set the working directory and add it to sys.path
project_path = "/storage/emulated/0/Sidekick Project Files"
if project_path not in sys.path:
    sys.path.append(project_path)
os.chdir(project_path)

from network_manager import NetworkManager
from data_handler import DataHandler
from security import SimpleSecurity
from belief_system import BeliefSystem
from language_model import LanguageModel  # ✅ Uses GPT-2 logic directly

# 🔹 Log file for recursive errors and trace debugging
LOG_FILE = os.path.join(project_path, "ui_bin.log")
TRACE_FILE = os.path.join(project_path, "trace_log.txt")  # New trace log

MEMORY_FILE = os.path.join(project_path, "sidekick_memory.json")  # ✅ Stores conversation history

# Setup logging for trace analysis
logging.basicConfig(filename=TRACE_FILE, level=logging.DEBUG, format="%(asctime)s - %(message)s")

def log_trace(message):
    """Logs trace messages for debugging loops."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] TRACE: {message}\n"
    
    with open(TRACE_FILE, "a") as log_file:
        log_file.write(log_entry)

def log_error(error_message):
    """Logs errors into ui_bin.log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR: {error_message}\n"

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

class SidekickUI:
    def __init__(self):
        print("Initializing Sidekick...")
        log_trace("Initializing SidekickUI...")

        try:
            # Initialize core components
            self.language_model = LanguageModel(model_dir=project_path)  # ✅ Handles GPT-2 internally
            self.data_handler = DataHandler(file_name=MEMORY_FILE)  # ✅ Tracks conversation history
            self.network_manager = NetworkManager(creator_id="Randell Murrin")
            self.security = SimpleSecurity(key="your-secret-key")
            self.belief_system = BeliefSystem()

            # 🔄 **Deferred Import to Prevent Circular Import Issue**
            from conversation_handler import ConversationHandler
            self.conversation_handler = ConversationHandler(language_model=self.language_model)
            
            self.running = True
            self.load_memory()  # ✅ Load past conversations for better context

            # Log initialization
            self.network_manager.log_event("Sidekick initialized successfully.")
            log_trace("Sidekick initialized successfully!")
            print("Sidekick initialized successfully!")

        except Exception as e:
            error_details = traceback.format_exc()
            log_error(error_details)  # Log error
            log_trace("Initialization failed!")
            print(f"An error occurred during initialization: {e}")
            self.running = False

    def load_memory(self):
        """Load Sidekick's conversation history for context retention."""
        log_trace("Loading memory...")
        
        if os.path.isfile(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r") as file:
                    self.memory = json.load(file)
                if not isinstance(self.memory, list):  # ✅ Ensure memory is a list
                    self.memory = []
                log_trace(f"Loaded {len(self.memory)} past conversations.")
                print(f"[Sidekick] Loaded {len(self.memory)} past conversations.")
            except json.JSONDecodeError:
                log_trace("Memory file corrupted. Resetting.")
                print("[Sidekick] Warning: Conversation memory corrupted. Resetting.")
                self.memory = []
        else:
            self.memory = []

    def save_memory(self, user_input, response):
        """Store each conversation turn to enhance Sidekick's learning."""
        log_trace(f"Saving memory: User: {user_input} | Sidekick: {response}")

        if not isinstance(self.memory, list):  # ✅ Prevent `dict has no attribute 'append'` error
            self.memory = []

        self.memory.append({"user": user_input, "sidekick": response})

        try:
            with open(MEMORY_FILE, "w") as file:
                json.dump(self.memory, file, indent=4)
        except Exception as e:
            log_error(f"Failed to save memory: {e}")

    def start(self):
        """Main interaction loop for Sidekick."""
        if not self.running:
            print("Failed to initialize Sidekick. Exiting...")
            return

        print("Hello, I'm Sidekick. How can I assist you today?")
        while self.running:
            try:
                user_input = self.get_input().strip()
                if not user_input:
                    continue  # Ignore empty input

                if user_input.lower() == "exit":
                    print("Goodbye!")
                    self.running = False
                    return

                log_trace(f"Received user input: {user_input}")

                # ✅ First, try conversation_handler (which calls GPT-2)
                response = self.conversation_handler.start_conversation(user_input)
                log_trace(f"Generated response (via conversation_handler): {response}")

                # 🔹 Ensure response isn't just mirrored input
                if response.strip().lower() == user_input.strip().lower():
                    log_trace("Detected possible recursion. Forcing GPT-2 response.")
                    response = self.language_model.generate_response(user_input)  # ✅ Force GPT-2 logic
                
                # ✅ Only log if response is valid
                if response and response.strip():
                    self.save_memory(user_input, response)

                print(response)

            except RecursionError as re:
                log_error(f"RecursionError: {re}")
                log_trace("Recursion error detected. Entering recovery mode.")
                print("⚠️ Recursive error detected. Entering recovery mode.")
                self.recover_from_recursion()

            except Exception as e:
                error_details = traceback.format_exc()
                log_error(error_details)  # Log error
                log_trace("Unexpected error occurred!")
                print(f"An unexpected error occurred: {e}")

    def recover_from_recursion(self):
        """Self-recovery process when a recursion error is detected."""
        log_trace("Recovering from recursion error.")
        print("It seems like I got stuck in a loop. Let's reset our conversation.")
        self.memory = []  # ✅ Clear memory to break the recursion loop
        self.running = True  # ✅ Keep running instead of crashing

    def get_input(self):
        """Capture user input via text only."""
        log_trace("Awaiting user input...")
        return input("> ")  # Only use text input

if __name__ == "__main__":
    sidekick = SidekickUI()
    sidekick.start()