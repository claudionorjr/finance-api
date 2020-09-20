from sqlalchemy.types import TypeDecorator, String
from app.common.cryptography import FernetEngine, AesEngine

class Encryptor(TypeDecorator):

    impl = String

    def process_bind_param(self, value, dialect):
        if value:
            return AesEngine().encrypt(value)
        return None

    def process_result_value(self, value, dialect):
        if value:
            return AesEngine().decrypt(value)
        return None
    

