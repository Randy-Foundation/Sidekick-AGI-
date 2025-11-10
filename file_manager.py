import os
import json
import hashlib
import time
from datetime import datetime
from belief_system import BeliefSystem
from memory_manager import MemoryManager

class FileManager:
    def __init__(self, root_directory="/storage/emulated/0/Sidekick_project_files"):
        """
        Initialize the File Manager to scan and analyze Sidekick's working directory.
        Includes security monitoring and learning-based classifications.
        """
        self.root_directory = root_directory
        self.belief_system = BeliefSystem()
        self.memory_manager = MemoryManager()
        self.file_metadata = {}

    # ======= DIRECTORY AND FILE SCANNING =======
    def scan_directory(self):
        """
        Scan the directory and retrieve all files while verifying integrity.
        This prevents unauthorized modifications and maintains security compliance.
        """
        files = []
        for root, dirs, file_names in os.walk(self.root_directory):
            for file_name in file_names:
                file_path = os.path.join(root, file_name)
                files.append(file_path)
                self.verify_file_integrity(file_path)  # Check if file has been tampered with
        return files

    def verify_file_integrity(self, file_path):
        """
        Compute hash of files and compare with stored values to detect unauthorized modifications.
        """
        if file_path in self.file_metadata:
            old_hash = self.file_metadata[file_path]["hash"]
        else:
            old_hash = None

        current_hash = self.compute_file_hash(file_path)
        if old_hash and old_hash != current_hash:
            print(f"[SECURITY ALERT]: Unauthorized modification detected in {file_path}!")
            # Take security action here (e.g., log event, restore file, alert user)

        # Store or update file metadata
        self.file_metadata[file_path] = {
            "hash": current_hash,
            "last_checked": datetime.now().isoformat()
        }

    def compute_file_hash(self, file_path):
        """
        Compute the SHA-256 hash of a file to track changes.
        """
        try:
            with open(file_path, "rb") as file:
                file_hash = hashlib.sha256(file.read()).hexdigest()
            return file_hash
        except Exception as e:
            print(f"[ERROR]: Could not compute hash for {file_path}: {e}")
            return None

    # ======= FILE READING & ANALYSIS =======
    def read_file(self, file_path):
        """
        Read the content of a given file based on its type.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"[ERROR]: Cannot read {file_path}: {e}")
            return None

    def analyze_files(self):
        """
        Analyze and classify all files in the directory, applying recursive learning where possible.
        """
        files = self.scan_directory()
        for file_path in files:
            content = self.read_file(file_path)
            if content:
                self.analyze_content(content, file_path)

    def analyze_content(self, content, file_path):
        """
        Analyze content dynamically and integrate it into Sidekick’s learning.
        """
        if file_path.endswith('.txt'):
            self.process_text(content, file_path)
        elif file_path.endswith('.json'):
            self.process_json(content, file_path)
        else:
            print(f"[INFO]: Skipping unknown file type {file_path}")

    def process_text(self, text, file_path):
        """
        Process and extract insights from text files.
        """
        print(f"[Processing] Analyzing text content from {file_path}")
        sentiment = self.memory_manager.analyze_text_sentiment(text)
        print(f"[INFO]: Detected Sentiment - {sentiment}")

    def process_json(self, json_data, file_path):
        """
        Handle JSON-based files and extract relevant learning.
        """
        try:
            data = json.loads(json_data)
            print(f"[Processing] JSON data loaded from {file_path}")
            self.memory_manager.store_knowledge(data)
        except json.JSONDecodeError as e:
            print(f"[ERROR]: JSON Decode Error in {file_path}: {e}")

    # ======= SELF-LEARNING & ADAPTATION =======
    def recursive_learning(self):
        """
        Apply recursive feedback to enhance Sidekick’s understanding from analyzed data.
        """
        files = self.scan_directory()
        for file_path in files:
            content = self.read_file(file_path)
            if content:
                self.memory_manager.integrate_knowledge(content)
                self.belief_system.validate_learning(content)

        # Memory management feedback
        self.memory_manager.optimize_memory_allocation()
        print("[INFO]: Recursive learning applied successfully.")

    # ======= SECURITY & FILE TRACKING =======
    def directory_monitor(self):
        """
        Monitor directory for any external modifications.
        """
        while True:
            print("[SECURITY]: Monitoring directory integrity...")
            time.sleep(60)  # Run check every minute
            self.scan_directory()

    def lock_unauthorized_access(self, file_path):
        """
        Lock file access if unauthorized modifications are detected.
        """
        try:
            os.chmod(file_path, 0o400)  # Read-only lock
            print(f"[SECURITY]: Locked file access to {file_path}")
        except Exception as e:
            print(f"[ERROR]: Could not lock file {file_path}: {e}")

# ======= EXAMPLE USAGE =======
if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.analyze_files()
    file_manager.recursive_learning()