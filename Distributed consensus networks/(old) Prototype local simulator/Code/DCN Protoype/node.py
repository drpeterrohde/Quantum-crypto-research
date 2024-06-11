#%% Importing local and non-local modules
import queue
from cryptography import *
from message import *
from public_data import *
# MOST RESTRUCTURING

#%% Defining the class which describes the individual nodes
class Node:
    
    # Defining the different type of information each node has
    def __init__(self, nodeID, network):
        self.nodeID = nodeID
        self.network = network
        self.channel = queue.Queue()
        self.commits = dict()
        self.publicData = PublicData()

    # Given a non-empty broadcast channel, record all messages and timestamp their arrival (nodes constantly listening & timestamping)
    def listen(self):
        while not self.channel.empty(): # while loop implies constant (each nodes have their own local interpretation)
            message = self.channel.get()
            self.publicData.push(message)
            self.timestamp(message)

    # Last step (compliance) theres nothing to commit-reveal, so you just announce your final measurements (who you think is compliant)
    def announce(self, statement):
        message = Message(self.nodeID, MessageType.ANNOUNCE, str(statement))
        self.network.broadcast(message)

    # Salt-hashes the message to be broadcast by the node onto the channel (commit their salted hash, cant take it back) (bid does it same)
    def commit(self, statement):
        salt = secret() #str(secrets.token_hex(salt_length))
        saltedHash = salted_hash(statement, salt)
        self.commits[str(statement)] = salt
        message = Message(self.nodeID, MessageType.COMMIT, saltedHash)
        self.network.broadcast(message)

    # Reveals if the output hashes that were commited actually satisfy the individuals salts of the nodes (reveal what the pre-image was)
    def reveal(self):
        for statement, salt in list(self.commits.items()):
            message = Message(self.nodeID, MessageType.REVEAL, statement, salt)
            self.network.broadcast(message)
            del self.commits[statement]

    # Timestamps the broadcast time of the node message
    def timestamp(self, message):
        if message.messageType != MessageType.TIMESTAMP:
            timestamp = Message(self.nodeID, MessageType.TIMESTAMP, message.digest())
            self.network.broadcast(timestamp)

    # Making random hash to get unique transaction ID (implicitly the commit)
    def bid(self):
        transactionID = secret() #str(secrets.token_hex(transaction_length)) # Dummy transaction ID
        salt = secret() #str(secrets.token_hex(salt_length))
        saltedHash = salted_hash(transactionID, salt)
        self.commits[transactionID] = salt
        message = Message(self.nodeID, MessageType.BID, saltedHash)
        self.network.broadcast(message)

    # Node gets information of who the other participants are
    def participants(self):
        myParticipants = list(map(lambda x: x[0], self.publicData.get_participants()))
        self.commit(myParticipants)
