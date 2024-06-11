from enum import Enum
import time
from cryptography import *

# MessageType enum
class MessageType(Enum):
    ANNOUNCE = 1
    COMMIT = 2
    REVEAL = 3
    TIMESTAMP = 4
    BID = 5
    PARTICIPANTS = 6

    def __str__(self):
        return f"{self.name}"

# Message class
class Message:
    def __init__(self, nodeID, messageType, statement, salt=""):
        self.nodeID = str(nodeID)
        self.messageType = messageType
        self.statement = statement
        self.salt = salt
        self.timestamp = time.time()

    def __str__(self):
        return f"[{self.nodeID}, {self.messageType}, {self.statement}, {self.timestamp}]"

    def digest(self):
        return hash(self)
