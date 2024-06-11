import queue
from cryptography import *
from message import *
from public_data import *

# Node class
class Node:
    def __init__(self, nodeID, network):
        self.nodeID = nodeID
        self.network = network
        self.channel = queue.Queue()
        self.commits = dict()
        self.publicData = PublicData()
        # Add keypair

    def listen(self):
        while not self.channel.empty():
            message = self.channel.get()
            self.publicData.push(message)
            self.timestamp(message)
            # Process message

    def announce(self, statement):
        message = Message(self.nodeID, MessageType.ANNOUNCE, str(statement))
        self.network.broadcast(message)

    def commit(self, statement):
        salt = secret() #str(secrets.token_hex(salt_length))
        saltedHash = salted_hash(statement, salt)
        self.commits[str(statement)] = salt
        message = Message(self.nodeID, MessageType.COMMIT, saltedHash)
        self.network.broadcast(message)

    def reveal(self):
        for statement, salt in list(self.commits.items()):
            message = Message(self.nodeID, MessageType.REVEAL, statement, salt)
            self.network.broadcast(message)
            del self.commits[statement]

    def timestamp(self, message):
        if message.messageType != MessageType.TIMESTAMP:
            timestamp = Message(self.nodeID, MessageType.TIMESTAMP, message.digest())
            self.network.broadcast(timestamp)

    def bid(self):
        transactionID = secret() #str(secrets.token_hex(transaction_length)) # Dummy transaction ID
        salt = secret() #str(secrets.token_hex(salt_length))
        saltedHash = salted_hash(transactionID, salt)
        self.commits[transactionID] = salt
        message = Message(self.nodeID, MessageType.BID, saltedHash)
        self.network.broadcast(message)

    def participants(self):
        myParticipants = list(map(lambda x: x[0], self.publicData.get_participants()))
        self.commit(myParticipants)
