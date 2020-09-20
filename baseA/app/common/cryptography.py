from app.config import Config
from cryptography.fernet import Fernet
import base64
import cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes


import six
import os

class FernetEngine:
    """
        Class created based on documentation from the cryptography library
        @see https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
        @see https://sqlalchemy-utils.readthedocs.io/en/latest/_modules/sqlalchemy_utils/types/encrypted/encrypted_type.html#EncryptedType
    """

    def encrypt(self, text):
        cipher_suite = Fernet(Config.CRYPT_KEY)
        cipher_text = cipher_suite.encrypt(text.encode())
        return cipher_text.decode()

    def decrypt(self, text_encrypted):
        cipher_suite = Fernet(Config.CRYPT_KEY)
        text_clean = cipher_suite.decrypt(text_encrypted.encode())
        return text_clean.decode()


class AesEngine:
    """
        Class created based on documentation from the cryptography library and sqlalchemy-utils
        @see https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
        @see https://sqlalchemy-utils.readthedocs.io/en/latest/_modules/sqlalchemy_utils/types/encrypted/encrypted_type.html#EncryptedType
    """

    def generate_key(self):
        key = Config.CRYPT_KEY
        key = key.encode()
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(key)
        engine_key = digest.finalize()

        return engine_key

    def encrypt(self, value):
        secret_key = self.generate_key()
        iv = secret_key[:12]
        cipher = Cipher(
            algorithms.AES(secret_key),
            modes.GCM(iv),
            backend=default_backend()
        )
        if not isinstance(value, six.string_types):
            value = repr(value)
        if isinstance(value, six.text_type):
            value = str(value)
        value = value.encode()
        encryptor = cipher.encryptor()

        encrypted = encryptor.update(value) + encryptor.finalize() 
        encrypted = base64.b64encode(encrypted).decode('ascii').strip()
        tag = base64.b64encode(encryptor.tag).decode('ascii').strip()
        return f'{tag}${encrypted}'

    def decrypt(self, value):
        secret_key = self.generate_key()
        iv = secret_key[:12]

        tag, encrypted_encode = value.split('$', 1)
        tag = base64.b64decode(tag)
        encrypted_decode = base64.b64decode(encrypted_encode)

        cipher = Cipher(
            algorithms.AES(secret_key),
            modes.GCM(iv, tag),
            backend=default_backend()
        )

        if isinstance(value, six.text_type):
            value = str(value)

        decryptor = cipher.decryptor()
        decrypted = decryptor.update(encrypted_decode) + decryptor.finalize()
    
        return decrypted.decode()


