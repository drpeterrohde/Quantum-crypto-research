#%% Importing local modules
from node import *

#%% Defining the class which describes the network of nodes
class Network:
    
    # Defining the amount of nodes in the network
    def __init__(self, nodeCount):
        self.nodes = [Node(i, self) for i in range(nodeCount)]

    # Putting a message on the collective broadcast channel for all the nodes to see
    def broadcast(self, message):
        print(message)
        for node in self.nodes:
            node.channel.put(message)

    # Updating the contents of the broadcast channel 
    def update(self):
        for node in self.nodes:
            node.listen()

    # Reveals the salts of the hashes put on the broadcast channel for the network to see
    def reveal(self):
        for node in self.nodes:
            node.reveal()

    # Collects all the bids of the nodes that wish to participate in consensus
    def bid(self):
        for node in self.nodes:
            node.bid()

    # Iterates through to see which of the nodes participate in consensus
    def participants(self):
        for node in self.nodes:
            node.participants()
