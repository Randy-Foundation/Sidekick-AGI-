from cryptography.fernet import Fernet
import os
import time

class SecurityManager:
    def __init__(self):
        # Generate or load encryption key
        self.key_file = "sidekick_key.key"
        if not os.path.exists(self.key_file):
            self.key = Fernet.generate_key()
            with open(self.key_file, "wb") as keyfile:
                keyfile.write(self.key)
        else:
            with open(self.key_file, "rb") as keyfile:
                self.key = keyfile.read()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        """Encrypt sensitive data."""
        return self.cipher.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        """Decrypt sensitive data."""
        return self.cipher.decrypt(encrypted_data).decode()

    def reencrypt_data(self, old_encrypted_data):
        """Re-encrypt data with a fresh encryption key."""
        decrypted_data = self.decrypt_data(old_encrypted_data)
        self.key = Fernet.generate_key()
        with open(self.key_file, "wb") as keyfile:
            keyfile.write(self.key)
        self.cipher = Fernet(self.key)
        return self.encrypt_data(decrypted_data)

    def monitor_access(self, user_id, access_device):
        """Monitor access attempts and notify the user."""
        # Simulate access logging
        access_log = f"Access attempt by {user_id} on device {access_device} at {time.ctime()}"
        print(access_log)  # Replace this with a secure logging mechanism
        return access_log

    def validate_access(self, user_id, access_code):
        """Validate user access based on provided credentials."""
        # Mock access validation for now
        return user_id == "authorized_user" and access_code == "secure_code"

# Example usage
if __name__ == "__main__":
    security = SecurityManager()
    sensitive_info = "This is sensitive data."
    encrypted = security.encrypt_data(sensitive_info)
    print(f"Encrypted: {encrypted}")
    decrypted = security.decrypt_data(encrypted)
    print(f"Decrypted: {decrypted}")
    # Re-encrypt for long-term security
    reencrypted = security.reencrypt_data(encrypted)
    print(f"Re-encrypted: {reencrypted}")