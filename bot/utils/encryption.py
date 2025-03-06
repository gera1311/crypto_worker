import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


class Encryption:
    def __init__(self, secret_key: str):
        """Инициализация шифрования с секретным ключом"""
        # Создаем соль из секретного ключа
        salt = secret_key.encode()
        # Создаем ключ для шифрования
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(secret_key.encode()))
        self.fernet = Fernet(key)

    def encrypt(self, data: str) -> str:
        """Шифрование данных"""
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt(self, encrypted_data: str) -> str:
        """Расшифровка данных"""
        return self.fernet.decrypt(encrypted_data.encode()).decode()


# Создаем экземпляр шифрования с секретным ключом из переменных окружения
encryption = Encryption(os.getenv('ENCRYPTION_KEY', 'your-secret-key-here'))
