# from enum import Enum
# import queue
# import secrets
# import time
# import statistics
# from operator import itemgetter

from cryptography import *
from message import *
from network import *
from public_data import *

# Main
network = Network(3)
network.bid()
network.update()
network.participants()
network.reveal()
C = network.nodes[0].publicData.random_subsets()
print(C)