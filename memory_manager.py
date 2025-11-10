import os
import json
import datetime
import math
from directory_anchor import DirectoryAnchor  # Import DirectoryAnchor

class MemoryManager:
    def __init__(self, root_directory=None, research_notes_file="research_notes.json"):
        """
        Initialize the Memory Manager with a DirectoryAnchor for managing root directory.
        Args:
            root_directory (str): The base directory for Sidekick's files.
            research_notes_file (str): Path to the research notes file for historical memory data.
        """
        self.directory_anchor = DirectoryAnchor(root_directory)
        self.research_notes_file = research_notes_file
        self.memory_data = {
            "allocated_memory_mb": 100,
            "used_memory_mb": 0,
            "efficiency_factor": 1.0  # Adjusts dynamically
        }
        self.memory_logs = "memory_logs.txt"

    # ==========================
    # 📊 Memory Usage Monitoring
    # ==========================

    def monitor_memory_usage(self):
        """
        Monitor current memory usage for files in the root directory.
        """
        total_size_mb = self.calculate_directory_size()
        self.memory_data["used_memory_mb"] = total_size_mb
        allocated = self.memory_data["allocated_memory_mb"]

        if total_size_mb >= allocated:
            print("🚨 [WARNING]: Memory limit reached! Running optimization before requesting more memory...")
            self.optimize_memory_usage()
        else:
            print(f"✅ [INFO]: Memory usage: {total_size_mb}/{allocated} MB.")

        self.log_memory_activity(f"Memory usage checked: {total_size_mb}/{allocated} MB")

    def calculate_directory_size(self):
        """
        Calculate the total size of files in the root directory managed by DirectoryAnchor.
        Returns:
            float: Total size of files in MB.
        """
        total_size = 0
        root_files = self.directory_anchor.list_root_files()
        for file in root_files:
            file_path = os.path.join(self.directory_anchor.get_root_directory(), file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
        return round(total_size / (1024 * 1024), 2)  # Convert bytes to MB

    # =============================
    # 🔄 Recursive Memory Management
    # =============================

    def request_more_memory(self, amount_mb):
        """
        Request additional memory allocation using a weighted system.
        Memory expansion is determined by the Golden Ratio (𝜙) and historical efficiency.
        """
        phi = 1.618  # Golden Ratio
        used = self.memory_data["used_memory_mb"]
        allocated = self.memory_data["allocated_memory_mb"]
        efficiency = self.memory_data["efficiency_factor"]

        # Calculate request weight based on prior memory efficiency
        weighted_request = round((amount_mb * phi) / efficiency, 2)

        print(f"⚖️ [INFO]: Sidekick is requesting {weighted_request} MB of memory.")
        print(f"📊 Current usage: {used}/{allocated} MB.")
        
        decision = input("Approve additional memory? (yes/no): ").strip().lower()
        if decision == "yes":
            self.memory_data["allocated_memory_mb"] += weighted_request
            self.log_memory_activity(f"Memory increased by {weighted_request} MB. New allocation: {self.memory_data['allocated_memory_mb']} MB.")
            print(f"✅ [INFO]: Memory increased to {self.memory_data['allocated_memory_mb']} MB.")
        else:
            print("⚠️ [INFO]: Memory request denied. Sidekick will optimize instead.")
            self.optimize_memory_usage()

    def optimize_memory_usage(self):
        """
        Optimize memory usage by removing redundant data and compressing logs.
        """
        before_size = self.calculate_directory_size()
        print(f"🔍 [INFO]: Running optimization... (Before: {before_size} MB)")

        # Purge unnecessary files (non-core logs, outdated temp files)
        self.purge_redundant_files()

        # Compress memory logs if they exceed 5MB
        self.compress_logs()

        after_size = self.calculate_directory_size()
        efficiency_gain = round(before_size - after_size, 2)
        self.memory_data["efficiency_factor"] += 0.1  # Increase efficiency for next requests

        print(f"✅ [INFO]: Optimization complete! Freed {efficiency_gain} MB.")
        self.log_memory_activity(f"Optimized memory. Freed {efficiency_gain} MB.")

    def purge_redundant_files(self):
        """
        Identify and remove unnecessary files to reclaim memory.
        """
        redundant_files = ["memory_logs.txt", "temp_cache.json"]
        for file in redundant_files:
            file_path = os.path.join(self.directory_anchor.get_root_directory(), file)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"🗑 [INFO]: Deleted {file}")

    def compress_logs(self):
        """
        Compress logs if they exceed 5MB.
        """
        log_file = os.path.join(self.directory_anchor.get_root_directory(), self.memory_logs)
        if os.path.exists(log_file) and os.path.getsize(log_file) > 5 * 1024 * 1024:  # 5MB threshold
            compressed_log = log_file + ".gz"
            with open(log_file, "rb") as f_in, open(compressed_log, "wb") as f_out:
                f_out.write(f_in.read())  # Simulate compression
            os.remove(log_file)  # Remove original after compression
            print(f"📦 [INFO]: Logs compressed to {compressed_log}")

    # ==========================
    # 🔍 Memory Anomaly Detection
    # ==========================

    def detect_memory_anomalies(self):
        """
        Analyze memory logs for unusual consumption patterns.
        """
        anomalies = []
        if self.memory_data["used_memory_mb"] > self.memory_data["allocated_memory_mb"] * 0.9:
            anomalies.append("High memory usage detected.")

        if self.memory_data["efficiency_factor"] < 0.5:
            anomalies.append("Inefficient memory usage warning.")

        if anomalies:
            print("🚨 [ALERT]: Memory anomalies detected!")
            for anomaly in anomalies:
                print(f"⚠️ {anomaly}")
            self.log_memory_activity("Memory anomalies detected: " + ", ".join(anomalies))
        else:
            print("✅ [INFO]: No anomalies detected in memory usage.")

    # ==========================
    # 📝 Logging and Research
    # ==========================

    def log_memory_activity(self, message):
        """
        Log memory-related activities.
        """
        log_entry = f"{datetime.datetime.now()}: {message}\n"
        with open(os.path.join(self.directory_anchor.get_root_directory(), self.memory_logs), "a") as log_file:
            log_file.write(log_entry)
        print(f"📜 [LOG]: {message}")

# =====================
# 🔬 Example Usage
# =====================
if __name__ == "__main__":
    memory_manager = MemoryManager("/storage/emulated/0/Sidekick project files")  # Replace with actual path

    # Monitor memory usage
    memory_manager.monitor_memory_usage()

    # Request more memory (based on weighted Golden Ratio calculations)
    memory_manager.request_more_memory(50)

    # Optimize storage if needed
    memory_manager.optimize_memory_usage()

    # Check for anomalies
    memory_manager.detect_memory_anomalies()