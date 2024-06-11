from node import *

# Network class
class Network:
    def __init__(self, nodeCount):
        self.nodes = [Node(i, self) for i in range(nodeCount)]

    def broadcast(self, message):
        print(message)
        for node in self.nodes:
            node.channel.put(message)

    def update(self):
        for node in self.nodes:
            node.listen()

    def reveal(self):
        for node in self.nodes:
            node.reveal()

    def bid(self):
        for node in self.nodes:
            node.bid()

    def participants(self):
        for node in self.nodes:
            node.participants()
