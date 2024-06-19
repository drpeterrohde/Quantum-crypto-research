#%% Importing local modules
from cryptography import *
from message import *
from network import *
from public_data import *

#%% Simulation of proof of consensus protocol via a fixed network size

# Initializing a network with 3 nodes
network = Network(3)

# Have nodes place initial bid to have a stake in the transaction and participate in consensus
network.bid()

# Checks
network.update()

#?
network.participants()

#?
network.reveal()

# Randomly assigned consensus network subsets
C = network.nodes[0].publicData.random_subsets()
print(C)