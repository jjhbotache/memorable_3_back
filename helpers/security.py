from cryptography.fernet import Fernet
import os
import dotenv
import base64
import hashlib


dotenv.load_dotenv()
SERVER_KEY = os.getenv("SERVER_KEY")


def get_key_from_env()->bytes:
    password_in_bytes = SERVER_KEY.encode()
    key = hashlib.sha256(password_in_bytes).digest()
    return base64.urlsafe_b64encode(key)


# Encriptar un mensaje
def encrypt_message(message: str) -> bytes:
    key = get_key_from_env()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Desencriptar un mensaje
def decrypt_message(encrypted_message: bytes ) -> str:
    key = get_key_from_env()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()
