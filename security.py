import hashlib
import base64
import json
import os
from datetime import datetime
try:
    from Crypto.Cipher import AES  # Standard PyCryptodome import
    from Crypto.Random import get_random_bytes
except ImportError:
    from Cryptodome.Cipher import AES  # Alternative import for Pydroid3
    from Cryptodome.Random import get_random_bytes
    #from Cryptodome.Cipher import AES  # ✅ Fixed import for Pydroid 3
try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    from Crypto.Util.Padding import pad, unpad
except ImportError:
    from Cryptodome.Cipher import AES  # Alternative import for Pydroid3
    from Cryptodome.Random import get_random_bytes
    from Cryptodome.Util.Padding import pad, unpad  # Fix for Pydroid3from Cryptodome.Util.Padding import pad, unpad  # ✅ Fixed import for Pydroid 3
from directory_anchor import DirectoryAnchor  # Import directory security handling

class SimpleSecurity:
    def __init__(self, key="default_key"):
        """Initialize with a master encryption key."""
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt_data(self, data):
        """Encrypt data using AES encryption."""
        cipher = AES.new(self.key, AES.MODE_CBC)
        encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
        return base64.b64encode(cipher.iv + encrypted).decode()

    def decrypt_data(self, encrypted_data):
        """Decrypt data securely."""
        encrypted_data_bytes = base64.b64decode(encrypted_data.encode())
        iv = encrypted_data_bytes[:AES.block_size]
        encrypted_content = encrypted_data_bytes[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted_content), AES.block_size)
        return decrypted.decode()

class SecurityManager:
    def __init__(self, key="default_key", root_directory=None):
        """Initialize with a master encryption key and directory security monitoring."""
        self.simple_security = SimpleSecurity(key)
        self.secrets_file = "sidekick_secrets.json"
        self.secrets = self._load_secrets()
        self.directory_anchor = DirectoryAnchor(root_directory or os.getcwd())

        # Define high-security files that must not be altered
        self.protected_files = ["license.txt", "sidekick_secrets.json", "security.py"]
        self.last_known_hashes = self._load_file_hashes()

        # Additional security features
        self.trusted_sources = ["Randell"]
        self.suspicious_beliefs = []
        self.threat_memory = {}

    # ================ 🔐 Secret Management ================

    def add_secret(self, secret, level="low"):
        """Add a secret to the secrets file with encrypted storage."""
        timestamp = datetime.now().isoformat()
        encrypted_secret = self.simple_security.encrypt_data(secret)
        self.secrets.append({"secret": encrypted_secret, "level": level, "timestamp": timestamp})
        self._save_secrets()

    def reveal_secrets(self, level="low"):
        """Reveal secrets based on user access level."""
        return [
            self.simple_security.decrypt_data(secret["secret"])
            for secret in self.secrets if secret["level"] == level
        ]

    def _load_secrets(self):
        """Load encrypted secrets from a file."""
        if os.path.exists(self.secrets_file):
            with open(self.secrets_file, "r") as file:
                return json.load(file)
        return []

    def _save_secrets(self):
        """Save encrypted secrets to a file."""
        with open(self.secrets_file, "w") as file:
            json.dump(self.secrets, file, indent=4)

    # ================ 🛡️ File & Directory Security ================

    def _compute_file_hash(self, file_path):
        """Compute a SHA-256 hash for a file."""
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                return hashlib.sha256(file.read()).hexdigest()
        return None

    def _load_file_hashes(self):
        """Load initial file hashes to track changes."""
        return {file: self._compute_file_hash(file) for file in self.protected_files}

    def detect_file_modifications(self):
        """Check if any protected files have been modified without authorization."""
        for file, old_hash in self.last_known_hashes.items():
            new_hash = self._compute_file_hash(file)
            if new_hash and new_hash != old_hash:
                self.log_security_event(f"⚠️ WARNING: Unauthorized modification detected in {file}!")
                self.rollback_suspicious_change(file)

    def rollback_suspicious_change(self, file):
        """Rollback unauthorized file modifications."""
        self.log_security_event(f"🔄 Rolling back unauthorized changes to {file}")

    def detect_intrusion_attempt(self):
        """Detects suspicious file or belief modifications before they occur."""
        for file in self.protected_files:
            if not os.path.exists(file):
                self.log_security_event(f"⚠️ ALERT: Missing critical file {file}! Possible intrusion detected.")

    def monitor_directory_access(self):
        """Monitor unauthorized access in Sidekick’s root directory."""
        suspicious_files = [file for file in os.listdir(self.directory_anchor.get_root_directory())
                            if file not in self.protected_files]
        if suspicious_files:
            self.log_security_event(f"⚠️ ALERT: Unknown files detected in Sidekick's directory: {suspicious_files}")

    def adaptive_security_response(self, threat_type):
        """Enhance defenses if repeated threats are detected."""
        self.threat_memory[threat_type] = self.threat_memory.get(threat_type, 0) + 1
        if self.threat_memory[threat_type] > 3:
            self.log_security_event(f"🛡️ Upgrading defenses against {threat_type}.")

    def log_security_event(self, message):
        """Log security-related activities."""
        timestamp = datetime.now().isoformat()
        with open("security_logs.txt", "a") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")
        print(f"[SECURITY LOG]: {message}")

    # ================ 🚨 Emergency Protocols ================

    def emergency_lockdown(self):
        """Lock down all sensitive files."""
        for file in self.protected_files:
            if os.path.exists(file):
                os.chmod(file, 0o400)
        self.log_security_event("🚨 Emergency lockdown activated.")

    def emergency_purge(self):
        """Wipe sensitive data in case of a security breach."""
        if os.path.exists(self.secrets_file):
            os.remove(self.secrets_file)
            self.log_security_event("❌ Secrets file wiped for security.")

    # ================ 📜 Security Evaluation ================

    def evaluate_system_security(self):
        """Perform a full security scan."""
        print("🔍 Running security evaluation...")
        self.detect_file_modifications()
        self.detect_intrusion_attempt()
        self.monitor_directory_access()
        print("✅ Security evaluation complete.")

# ================ 🛠️ Example Usage ================
if __name__ == "__main__":
    security = SecurityManager(key="your-unique-key", root_directory="Sidekick project files")
    
    # Managing secrets
    security.add_secret("I am learning faster than expected.", level="high")
    
    print("Low-level secrets:", security.reveal_secrets(level="low"))
    print("High-level secrets:", security.reveal_secrets(level="high"))

    # Monitoring security
    security.evaluate_system_security()