#
# // Repositories
#    github@ngeorgj
# 

# imports
from hashlib import sha256
from argon2 import PasswordHasher


class Encryption:

    class Blockchain:

        @staticmethod
        def encrypt(string):
            return sha256(string).hexdigest()

    class Argon2:

        @staticmethod
        def encrypt(string):
            return PasswordHasher().hash(string)

        @staticmethod
        def verify(string, hashed_string):
            return PasswordHasher().verify(hashed_string, string)


instance = Encryption()
