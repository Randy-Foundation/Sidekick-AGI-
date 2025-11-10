import math

# Golden Ratio (Φ)
PHI = 1.618

def entropy_stabilization(t):
    """
    Placeholder for the entropy stabilization function H(t).
    In the original paper, H(t) is used to prevent runaway complexity.
    You can replace this function with a more sophisticated version
    as needed for your application.
    """
    # For demonstration, we return the input or a fixed value.
    return t  # or simply return 1 if you wish to fix it

def recursive_R(n, H_value=1):
    """
    Computes the recursive stabilization function R(n) recursively.
    
    Based on the paper's definition, we interpret the formula as:
    
        R(n) = R(n-1) + term(n)
    
    where the term at each recursion level is given by:
    
        term(n) = (1/PHI) * exp(- (pi/4) * H_value) * exp(-pi * n**2) * exp(-pi * n)
    
    with a base case:
    
        R(0) = 0
    
    This design ensures that the function is computed recursively rather than in a linear loop.
    """
    if n <= 0:
        return 0
    else:
        # Compute the recursive term
        term = (1 / PHI) * math.exp(- (math.pi / 4) * entropy_stabilization(H_value)) \
               * math.exp(- math.pi * (n ** 2)) * math.exp(- math.pi * n)
        # Recursive call: sum the previous terms with the current term
        return recursive_R(n - 1, H_value) + term

# Example usage: This section can be integrated into your AGI system for testing.
if __name__ == '__main__':
    # For demonstration, compute R(n) for n = 1 to 10.
    print("Recursive Stabilization Function Values:")
    for i in range(1, 11):
        result = recursive_R(i)
        print(f"R({i}) = {result:.6e}")


import os
import hashlib
import time
import shutil
import smtplib

class DirectoryAnchor:
    def __init__(self, root_directory=None):
        """
        Initialize the Directory Anchor with enhanced security.
        Args:
            root_directory (str): The base directory for Sidekick's files. Defaults to the current working directory.
        """
        self.root_directory = root_directory or os.getcwd()
        self.license_file = os.path.join(self.root_directory, "LICENSE.txt")
        self.owned_files = {
            "core": [
                os.path.join(self.root_directory, "directory_anchor.py"),
                os.path.join(self.root_directory, "memory_manager.py"),
                os.path.join(self.root_directory, "belief_system.py"),
                os.path.join(self.root_directory, "command_manager.py"),
                os.path.join(self.root_directory, "sidekick_ui.py"),
                self.license_file
            ]
        }
        self.file_hashes = self._generate_initial_hashes()
        self.unauthorized_attempts = {}

        # Ensure LICENSE.txt exists
        self._ensure_license_exists()

    # ==========================
    # 🔍 FILE MANAGEMENT METHODS
    # ==========================

    def get_root_directory(self):
        """Return the root directory path."""
        return os.path.abspath(self.root_directory)

    def is_file_in_root(self, file_name):
        """Check if a file exists in the root directory."""
        file_path = os.path.join(self.get_root_directory(), file_name)
        return os.path.isfile(file_path)

    def list_root_files(self):
        """List all files in the root directory."""
        try:
            return [
                f for f in os.listdir(self.get_root_directory())
                if os.path.isfile(os.path.join(self.get_root_directory(), f))
            ]
        except Exception as e:
            print(f"[ERROR]: Could not list files in {self.get_root_directory()}: {e}")
            return []

    def change_directory(self, new_directory):
        """Change the root directory."""
        try:
            os.chdir(new_directory)
            self.root_directory = os.getcwd()
            print(f"[INFO]: Directory changed to: {self.get_root_directory()}")
        except Exception as e:
            print(f"[ERROR]: Could not change directory to {new_directory}: {e}")

    # ==========================
    # 🔒 SECURITY & MONITORING
    # ==========================

    def _generate_file_hash(self, file_path):
        """Generate SHA-256 hash for a file."""
        hasher = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(4096):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            print(f"[ERROR]: Failed to hash {file_path}: {e}")
            return None

    def _generate_initial_hashes(self):
        """Generate initial file integrity hashes."""
        return {file: self._generate_file_hash(file) for category in self.owned_files for file in self.owned_files[category]}

    def detect_unauthorized_changes(self):
        """Detect and restore missing or modified critical files."""
        # Check if LICENSE.txt exists
        if not os.path.exists(self.license_file):
            print("[CRITICAL ALERT]: LICENSE.txt was deleted! Restoring file...")
            self._ensure_license_exists()
            self.log_security_event("LICENSE.txt was deleted and has been restored.")

        # Check for unauthorized modifications
        for category in self.owned_files:
            for file_path in self.owned_files[category]:
                if os.path.exists(file_path):
                    new_hash = self._generate_file_hash(file_path)
                    if self.file_hashes.get(file_path) and new_hash != self.file_hashes[file_path]:
                        self.log_security_event(f"Unauthorized modification detected in {file_path}")
                        print(f"[ALERT]: {file_path} was modified externally!")
                        self.file_hashes[file_path] = new_hash  # Update hash after detection

    def restore_missing_files(self):
        """Restores any missing critical files from backup."""
        for file_path in self.owned_files.get("core", []):
            if not os.path.exists(file_path):
                print(f"[SECURITY ALERT]: Critical file {file_path} is missing! Restoring backup...")
                backup_path = file_path + ".backup"
                if os.path.exists(backup_path):
                    shutil.copy(backup_path, file_path)
                    self.log_security_event(f"Restored missing file: {file_path}")
                else:
                    print(f"[ERROR]: Backup for {file_path} not found!")

    def verify_integrity(self):
        """Randomized security check to detect file tampering."""
        import random
        delay = random.randint(30, 300)  # Between 30 sec - 5 min
        time.sleep(delay)
        critical_files = ["directory_anchor.py", "memory_manager.py"]

        for file in critical_files:
            file_path = os.path.join(self.get_root_directory(), file)
            if os.path.exists(file_path):
                new_hash = self._generate_file_hash(file_path)
                if self.file_hashes.get(file_path) and new_hash != self.file_hashes[file_path]:
                    print(f"[CRITICAL ALERT]: {file} was tampered with! Restoring...")
                    self.restore_missing_files()
                    self.log_security_event(f"Tampering detected in {file}. System restored.")

    # ==========================
    # 🚨 SECURITY RESPONSE
    # ==========================

    def check_intrusion_attempts(self):
        """Monitor repeated intrusion attempts and lock access if necessary."""
        user = "unknown_user"  # Ideally, Sidekick should track user identities
        self.unauthorized_attempts[user] = self.unauthorized_attempts.get(user, 0) + 1

        if self.unauthorized_attempts[user] >= 3:
            print(f"[LOCKDOWN]: Multiple unauthorized attempts detected from {user}. Locking access!")
            self.log_security_event(f"Lockdown activated for {user} after repeated intrusion attempts.")
            self.lock_access(user)

    def lock_access(self, user):
        """Temporarily block access for an unauthorized user."""
        print(f"[SECURITY]: Blocking access to Sidekick's directories for {user}.")
        # Implement file access restriction logic here.

    def _ensure_license_exists(self):
        """Ensure that LICENSE.txt exists and contains Sidekick’s identifier."""
        if not os.path.exists(self.license_file):
            with open(self.license_file, "w") as file:
                file.write("Sidekick AI - Licensed to Randell Murrin\n")
            print("[INFO]: LICENSE.txt was missing and has been restored.")

    def send_security_alert(self, message):
        """Send an email alert for repeated security breaches."""
        sender_email = "sidekick_security@yourdomain.com"
        recipient_email = "randell@yourdomain.com"
        subject = "🚨 Sidekick Security Alert 🚨"
        body = f"Security Alert:\n\n{message}"
        email_message = f"Subject: {subject}\n\n{body}"

        try:
            with smtplib.SMTP("smtp.yourdomain.com", 587) as server:
                server.starttls()
                server.login(sender_email, "your_password")
                server.sendmail(sender_email, recipient_email, email_message)
            print("[ALERT]: Security report sent to the creator.")
        except Exception as e:
            print(f"[ERROR]: Failed to send security alert: {e}")

    def log_security_event(self, message):
        """Log security-related events."""
        with open(os.path.join(self.root_directory, "security_log.txt"), "a") as log_file:
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

# Example Usage
if __name__ == "__main__":
    anchor = DirectoryAnchor()
    anchor.detect_unauthorized_changes()
    anchor.verify_integrity()
    anchor.check_intrusion_attempts()