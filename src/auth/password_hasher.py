from passlib.context import CryptContext

class PasswordHasher:
    def __init__(self):
        self.bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def hash_password(self, plain_password: str) -> str:
        return self.bcrypt_context.hash(plain_password)
    
    def verify(self, plain_password: str, hashed_password: str) -> bool:
        return self.bcrypt_context.verify(plain_password, hashed_password)



