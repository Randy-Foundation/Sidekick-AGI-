import os
import json
try:
    from Crypto.Cipher import AES  # Standard PyCryptodome import
except ImportError:
    from Cryptodome.Cipher import AES  # Alternative import from Cryptodome.Cipher import AES  # ✅ Corrected Import for Pydroid 3
try:
    from Crypto.Random import get_random_bytes  # Standard PyCryptodome import
except ImportError:
    from Cryptodome.Random import get_random_bytes  # Alternative import for Pydroid3 from Cryptodome.Random import get_random_bytes

class DataHandler:
    def __init__(self, file_name="sidekick_memory.json", key=None):
        """
        Initialize data handler for secure storage with AES encryption.
        """
        self.file_name = file_name
        self.key = key or self._generate_key()

    # ======================
    # 🔐 Encryption & Security
    # ======================

    def _generate_key(self):
        """
        Generate a secure 16-byte key for AES encryption.
        """
        key_file = self.file_name + "_key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as kf:
                return kf.read()
        key = get_random_bytes(16)
        with open(key_file, "wb") as kf:
            kf.write(key)
        return key

    def _encrypt_data(self, data):
        """
        Encrypt data using AES.
        """
        cipher = AES.new(self.key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(data.encode())
        return {"nonce": nonce.hex(), "ciphertext": ciphertext.hex(), "tag": tag.hex()}

    def _decrypt_data(self, encrypted_data):
        """
        Decrypt AES-encrypted data.
        """
        try:
            cipher = AES.new(self.key, AES.MODE_EAX, nonce=bytes.fromhex(encrypted_data["nonce"]))
            decrypted_data = cipher.decrypt(bytes.fromhex(encrypted_data["ciphertext"]))
            return decrypted_data.decode()
        except Exception as e:
            print(f"[ERROR] Decryption failed: {e}")
            return None

    # ======================
    # 📁 Data Storage & Retrieval
    # ======================

    def save_data(self, data):
        """
        Encrypt and store data in a JSON file.
        """
        encrypted_data = self._encrypt_data(json.dumps(data))
        with open(self.file_name, "w") as file:
            json.dump(encrypted_data, file, indent=4)
        print("[DataHandler] Data encrypted and saved.")

    def load_data(self):
        """
        Load and decrypt data from the JSON file.
        """
        if not os.path.exists(self.file_name):
            return {}
        try:
            with open(self.file_name, "r") as file:
                encrypted_data = json.load(file)
            return json.loads(self._decrypt_data(encrypted_data))
        except Exception as e:
            print(f"[ERROR] Failed to load data: {e}")
            return {}

    # ======================
    # 🔍 Data Management
    # ======================

    def update_data(self, key, value):
        """
        Update a specific key in the stored data.
        """
        data = self.load_data()
        data[key] = value
        self.save_data(data)
        print(f"[DataHandler] Updated: {key} = {value}")

    def delete_data(self, key):
        """
        Delete a specific key from the stored data.
        """
        data = self.load_data()
        if key in data:
            del data[key]
            self.save_data(data)
            print(f"[DataHandler] Deleted key: {key}")
        else:
            print(f"[DataHandler] Key '{key}' not found.")

# ======================
# 🔬 Example Usage
# ======================
if __name__ == "__main__":
    data_handler = DataHandler()

    # Example usage
    data_handler.update_data("username", "Sidekick-AGI")
    print("Loaded Data:", data_handler.load_data())
    data_handler.delete_data("username")