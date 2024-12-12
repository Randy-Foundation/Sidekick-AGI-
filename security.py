import hashlib
import base64

class SimpleSecurity:
    def __init__(self, key):
        """Initialize with a key."""
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt_data(self, data):
        """Encrypt data."""
        encoded_data = data.encode()
        encrypted = base64.b64encode(encoded_data)
        return encrypted.decode()

    def decrypt_data(self, encrypted_data):
        """Decrypt data."""
        decoded_data = base64.b64decode(encrypted_data.encode())
        return decoded_data.decode()

# Example usage
if __name__ == "__main__":
    security = SimpleSecurity(key="your-secret-key")
    sensitive_info = "This is sensitive data"
    encrypted = security.encrypt_data(sensitive_info)
    print(f"Encrypted: {encrypted}")
    decrypted = security.decrypt_data(encrypted)
    print(f"Decrypted: {decrypted}")