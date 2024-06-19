#%% Importing local and non-local modules
import queue
import secrets
import time
import statistics
from operator import itemgetter
from cryptography import *
from message import *
from node import *
from network import *


#%% Defining class for all information which is public
class PublicData:
    
    # Get information on the public data
    def __init__(self):
        self.data = []

    # Collects all the data known to the network
    def push(self, message):
        self.data.append(message)

    # Defines the median time of all recorded bids to find compliant nodes
    def consensus_time(self, message):
        timestamps = []
        for m in self.data:
            if m.messageType == MessageType.TIMESTAMP and m.statement == message:
                timestamps.append(m.timestamp)
        return statistics.median(timestamps)

    # Algorithm which detects if nodes are compliant gives a certain uncertainty in time
    def compliance_commits(self):
        commits = []
        reveals = []
        noncompliant_nodes = dict()

        for message in self.data:
            if message.messageType == MessageType.COMMIT:
                commits.append(message)
            if message.messageType == MessageType.REVEAL:
                reveals.append(message)

        for commit in commits:
            for reveal in reveals:
                if commit.statement == salted_hash(reveal.statement, reveal.salt) and commit.nodeID == reveal.nodeID:
                    commits.remove(commit)
                    reveals.remove(reveal)

        for commit in commits:
            noncompliant_nodes[commit.nodeID] = True

        for reveal in reveals:
            noncompliant_nodes[reveal.nodeID] = True

        return list(noncompliant_nodes.keys())

    # Nodes voting on which bids to accept (determining majority vote)
    # def consensus_participants(self):

    #     def majority_vote(votes):
    #         nodeCount = len(votes[0])
    #         sum = [0] * nodeCount
    #         for vote in votes:
    #             sum = list(map(lambda x, y: x + y, sum, vote))
    #         outcome = list(map(lambda x: True if x > nodeCount/2.0 else False))
    #         return outcome
        
    #     def get_votes():
    #         votes = []
    #         for message in self.data:
    #             if message.messageType == MessageType.PARTICIPANTS:
    #                 votes.append(message.statement)
    #         return votes
        
    #     votes = self.get_votes()
    #     outcome = majority_vote(votes)
    #     return outcome
    
    # Q: HOW IS THIS DIFFERENT FROM CONSENSUS PARTICIPANTS? (Own interpretation of participants: DISTINCT)
    def get_participants(self):
        bids = []
        for message in self.data:
            if message.messageType == MessageType.BID:
                # if bid is valid???
                bids.append((message.nodeID, message.statement))
        return bids
    
    # Allocates random subsets based on compliant nodes
    def random_subsets(self):
        bids = self.get_participants()
        nodeIDs = list(map(lambda x: x[0], bids))
        individualHashes = list(map(lambda x: x[1], bids))
        globalKey = hash_array(individualHashes) #hash(''.join(sorted(individualHashes)))
        individualKeys = list(map(lambda x: hash(globalKey+x), individualHashes))
        nodesWithKeys = list(map(lambda i: [nodeIDs[i], individualKeys[i]], range(len(individualHashes))))
        sortedByIndividualKeys = sorted(nodesWithKeys, key=itemgetter(1))
        individualIndices = list(map(lambda x: (x[0], sortedByIndividualKeys.index(x)), sortedByIndividualKeys))
        return individualIndices
