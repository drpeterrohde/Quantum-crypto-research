#%% Importing non-local modules
import hashlib
import secrets

#%% Defining constants used in function defitions
SECRET_LENGTH = 4
SALT_LENGTH = 4
TRANSACTION_LENGTH = 4

#%% Defining cryptographic functions used for consensus protocols

# Hash fuction
def hash(x):
    
    # Outputs a unique hash for a given input
    return str(hashlib.sha256(str(x).encode()).hexdigest())[0:7]

# Salted hash
def salted_hash(x, salt):
    
    # Outputs a salted hash for each node to announce
    return hash(str(x) + str(salt))

# Hash array
def hash_array(x):
    
    # Ordered array of input strings
    sortedInputs = sorted(x)
    
    # Concatenating array elements
    concatenatedSortedInputs = ''.join(sortedInputs)
    
    # Combining hash information in truncated set
    return hash(concatenatedSortedInputs)

# Generate fixed-length secret
def secret():
    
    # Generating fixed-length secret (Q: IS THIS FOR THE CLAW-FREE FUNCTION FORMALISM?)
    return str(secrets.token_hex(SECRET_LENGTH))
