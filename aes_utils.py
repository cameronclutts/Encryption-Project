import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AESUtils:
    BLOCK_SIZE = 16  # AES block size

    def __init__(self, key: bytes):
        if not isinstance(key, bytes) or len(key) != 32:
            raise ValueError("Key must be 32 bytes (256 bits).")
        self.key = key

    def encrypt(self, message: str) -> str:
        iv = get_random_bytes(self.BLOCK_SIZE)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(message.encode(), self.BLOCK_SIZE))
        return base64.b64encode(iv + ciphertext).decode()

    def decrypt(self, encoded: str) -> str:
        try:
            raw = base64.b64decode(encoded)
            iv = raw[:self.BLOCK_SIZE]
            ciphertext = raw[self.BLOCK_SIZE:]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(ciphertext), self.BLOCK_SIZE).decode()
        except Exception as e:
            return f"[Decryption failed] {str(e)}"
