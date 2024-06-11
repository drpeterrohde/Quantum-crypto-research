import hashlib
import secrets

# Constants
SECRET_LENGTH = 4
# SALT_LENGTH = 4
# TRANSACTION_LENGTH = 4

# Hash fuction
def hash(x):
    return str(hashlib.sha256(str(x).encode()).hexdigest())[0:7]

# Salted hash
def salted_hash(x, salt):
    return hash(str(x) + str(salt))

# Hash array
def hash_array(x):
    # Lexigraphical order of input strings
    sortedInputs = sorted(x)
    # Concatenate array elements
    concatenatedSortedInputs = ''.join(sortedInputs)
    # Combined hash
    return hash(concatenatedSortedInputs)

# Generate fixed-length secret
def secret():
    return str(secrets.token_hex(SECRET_LENGTH))
