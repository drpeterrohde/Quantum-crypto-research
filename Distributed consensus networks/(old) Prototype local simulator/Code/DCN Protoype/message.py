#%% Importing local & non-local modules
from enum import Enum
import time
from cryptography import * #R: THIS METHOD OF IMPORTING WILL CAUSE PERFORMANCE ISSUES!

#%% Defining the class which determines the structure of messages on a shared broadcast channel

# Defining the class which is responsible for the type of message (Q: IS IT REALLY NECESSARY TO SPLIT THIS INFORMATION INTO A CLASS OF ITS OWN AND NOT HAVE ONE ENCOMPASSING CLASS?)
class MessageType(Enum):#Assigning reabale labels with numbers for users
    
    # Announce in a shared channel interest to participate in consensus
    ANNOUNCE = 1
    
    # Initial bid with a salted-hash 
    COMMIT = 2
    
    # Input of the salt-hash to confirm the validity of initial bid 
    REVEAL = 3
    
    # Timestamp at which the message was sent on the broadcast channel
    TIMESTAMP = 4
    
    # Amount bid to be considered for parcitipation 
    BID = 5
    
    # The ammount of participants which observe messages on the channel (Q: IS THIS CORRECT?)
    PARTICIPANTS = 6

    # Extracting the information for the message type
    def __str__(self):
        return f"{self.name}"

# Defining the class of the messages on the broacast channel
class Message:
    
    # Defining different type of information of the message
    def __init__(self, nodeID, messageType, statement, salt=""):
        
        # Index identity of the node in the network that sent the message
        self.nodeID = str(nodeID)
        
        # What type of information is extracted from the message
        self.messageType = messageType
        
        # Q: STATEMENT OF ANNOUCEMENT AND COMMIT?
        self.statement = statement
        
        # Q: YOU CAN EXTRACT THE SALT FROM OTHER NODES HASH???
        self.salt = salt
        
        # Time at which the message was sent on the broadcast channel
        self.timestamp = time.time()

    # Defining all the information of the message in an array
    def __str__(self):
        return f"[{self.nodeID}, {self.messageType}, {self.statement}, {self.timestamp}]"
    
    # Outputs the hash of the message (Q: WHY MUST THIS BE A SEPARATE FUNCTION?)
    def digest(self):
        return hash(self)
