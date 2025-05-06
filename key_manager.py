import os

class KeyManager:
    def __init__(self, key_file: str = "shared.key"):
        self.key_file = key_file

    def generate_key(self) -> tuple[bool, str]:
        if os.path.exists(self.key_file):
            return False, f"Key file '{self.key_file}' already exists."
        key = os.urandom(32)
        with open(self.key_file, "wb") as f:
            f.write(key)
        return True, f"Key file '{self.key_file}' generated successfully."

    def load_key(self) -> bytes | None:
        if not os.path.exists(self.key_file):
            return None
        with open(self.key_file, "rb") as f:
            key = f.read()
        if len(key) != 32:
            return None
        return key
