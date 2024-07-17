#%% Importing modules - コンプリート

import numpy as np
import copy


# %% Defining the networks, their trust, and their security - コンプリート

# Defining the networks and their elements
N = [0,1,2] # Network N with nodes: i,j,k
M = [3,4] # Network M with nodes: l,m

# Defining node-respective empty sets
emptySets = {k:[] for k in range(len(N)+len(M))}

# Defining all trust matrix permutations
trustNinN = np.array([
    [0,1/2,1/4],
    [1/3,0,1/4],
    [1/2,1,0]
])
trustMinM = np.array([
    [0,1/4],
    [1/3,0]
])
trustNinM = np.array([
    [1,1/5],
    [1/3,1/2],
    [1/3,1]
])
trustMinN = np.array([
    [1/7,1/2,1/3],
    [1,1/4,1/2]
])

# Combining trust matrices into one total one
systemTrust = np.hstack((
    np.vstack((trustNinN,trustMinN)), np.vstack((trustNinM,trustMinM))
))

# Defining the security parameters of the nodes in the network
securityN = {0:1/6,1:1/2,2:1/3}
securityM = {3:1/2,4:1/4}
nodeSecurity = securityN | securityM

# Defining the network wide security parameters via most lenient n/2
orderedSecurityN = sorted(list(securityN.values()))
orderedSecurityM = sorted(list(securityM.values()))
securityNetworkN = np.max(orderedSecurityN[int(len(orderedSecurityN)/2):])
securityNetworkM = np.max(orderedSecurityM[int(len(orderedSecurityM)/2):])
networkSecurity = {0:securityNetworkN,1:securityNetworkM}

# Printing the outcome of definitions
print('Trust of network N in itself')
print(trustNinN)
print('Trust of network M in itself')
print(trustMinM)
print('Trust of network N in M')
print(trustNinM)
print('Trust of network M in N')
print(trustMinN)
print('Total trust matrix')
print(systemTrust)
print('Possible empty sets')
print(emptySets)
print('Security parameters nodes')
print(nodeSecurity)
print('Security parameters networks')
print(networkSecurity)


# %% Defining the different scale trust functions - コンプリート

# Defining the trust function between nodes and networks
def r(trustAinB, forward=True):
    
    # Computing the r_i(B) values for all nodes i in A
    if forward == True:
        
        # Initializing the network and empty trust values
        networkSize = len(trustAinB) #|A|
        trustValues = np.zeros(networkSize)
        for i in range(networkSize):
            trustValues[i] =  1/(networkSize) * np.sum(trustAinB[i])
            # {r_i(B),...,r_k(B)}
             
    # Computing the r_A(j) values for all nodes j in B
    if forward == False:
        
        # Initializing the network and empty trust values
        networkSize = len(trustAinB.T) #|B|
        trustValues = np.zeros(networkSize)
        for j in range(networkSize):
            trustValues[j] =  1/(networkSize) * np.sum(trustAinB.T[j])
            # {r_A(l),...,r_A(m)}
    
    # Returning the desired trust array
    return trustValues

# Defining the trust function between networks   
def rr(trustAinB, trustBinA, forward=True):
    
    # Computing the r_i(N) sums amongst the networks
    trustIinB = r(trustAinB) # {r_i(B),...,r_k(B)}
    trustJinA = r(trustBinA) # {r_l(A),...,r_m(A)}
    
    # Computing the trust between networks as r(A,B)
    if forward == True:
        networkTrustAinB = np.max(trustIinB)
        
        # Returning the network wide trust of A in B
        return networkTrustAinB
    
    # Computing the trust between networks as r(B,A)
    if forward == False:
        networkTrustBinA = np.max(trustJinA)
        
        # Returning the network wide trust of B in A
        return networkTrustBinA

# Defining the boolean decision function between nodes and networks
def f(trustAinB, nodesSecurity, networksSecurity, forward=True):
    
    # Computing the trust between the networks
    trustIinB = r(trustAinB) # {r_i(B),...,r_k(B)}
    trustAinJ = r(trustAinB, False) # {r_A(l),...,r_A(m)}
    
    # Computing the booleans based on r_i(B)
    if forward == True:
        
        # Initializing the network size and boolean array
        networkSize = len(trustAinB) #|A|
        nodeBoolean = np.zeros(networkSize)
        
        # Looping through boolean images for all nodes i in A
        for i in range(networkSize):
            if trustIinB[i] <= nodesSecurity[i]:
                nodeBoolean[i] = 1
                
        # Returning the boolean decisions of the nodes
        return nodeBoolean
    
    # Computing the booleans based on parameters r_A(j)
    if forward == False:
        
        # Initializing the network size and boolean array
        networkSize = len(trustAinB.T) #|B|
        networkBoolean = np.zeros(networkSize)
        
        # Looping through boolean images for all nodes j in B
        for j in range(networkSize):
            if trustAinJ[j] <= networksSecurity:
                networkBoolean[j] = 1
        
        # Returning the boolean decisions of the network 
        return networkBoolean

# Testing the functions on the initialized network distribution
print('--- Trust of nodes amongst same network ---')
print('Trusts of nodes in their own network')
print(
    r(trustNinN)
    )
print('Trust of a network in its nodes')
print(
    r(trustNinN,False)
    )
print('Security parameters of nodes in network N')
print(
    securityN
    )
print('Security parameters of network N')
print(
    securityNetworkN
)
print('--- Boolean decision outcome ---')
print('Node wide decisions')
print(
    f(trustNinN, securityN, securityNetworkN)
    )
print('Network wide decisions')
print(
    f(trustNinN, securityN, securityNetworkN, False)
    )
print('--- Trust between different networks ---')
print('Trust of network N in network M')
print(
    rr(trustNinM,trustMinN)
    )
print('Trust of network M in network N')
print(
    rr(trustNinM,trustMinN,False)
    )


# %% Defining the network partitioning algorithm - コンプリート

# Defining the function which repartitions groups of networks
def networkPartition(networks,videSets,trustMatrix, nodesSecurity, networksSecurity):
    
    # Initializing copies of input data
    A,B = [network for network in networks]
    newA,newB = A.copy(),B.copy()
    nullSets = copy.deepcopy(videSets)
    
    # Printing intial configuration of networks 
    print('--- Original state of networks ---')
    print('Initial network N: ', A)
    print('Initial network M: ', B)
    print('Initial empty sets: ', videSets)
    
    # Extracting block trust matrices from total trust matrix
    trustAinA = trustMatrix[:len(A), :len(A)]
    trustAinB = trustMatrix[:len(A), len(A):len(A) + len(B)]
    trustBinA = trustMatrix[len(A):len(A) + len(B), :len(A)]
    
    # Computing node wide trust values for all nodes i in A
    trustIinA = r(trustAinA) # {r_i(A),r_j(A),r_k(A)}
    trustIinB = r(trustAinB) # {r_i(B),r_j(B),r_k(B)}
    
    # Computing network wide trust values
    trustBinI = r(trustBinA, False) # {r_B(i),r_B(j),r_B(k)}
    
    # Computing optimal locations for all nodes i in A
    jumpLocations = [[trustIinA[i], trustIinB[i]] for i in range(len(A))]
    optimalLocations = [loc.index(min(loc)) for loc in jumpLocations]
    
    # Performing jumps if optimal location network accepts
    for i in A:
        
        # Extacting the index of node i
        nodeIndex = A.index(i)
        
        # Selecting optimal location for node i in A
        location = optimalLocations[nodeIndex] #0 for A, 1 for B
        
        # Non-empty location condition
        if location != 0:
            print('Node', A[nodeIndex], 'in network N wants to jump to network M.')
            
            # Seeing validity of trust condition
            if trustBinI[nodeIndex] <= networksSecurity[location]:
                
                # Moving node i from A to B
                jumpNode = newA.pop(nodeIndex)
                newB.insert(len(newB), jumpNode)
                print('Node', A[nodeIndex], 'has jumped to network M!')
    
    # Seeing if nodes want to leave their own network into an empty set
    for i in A:

        # Only looking at nodes which were originally there
        if i in newA:
            
            # Extracting the index of node i
            nodeIndex = A.index(i)
            
            # Seeing validity of trust conditions
            if trustIinA[nodeIndex] > nodesSecurity[i]:
                
                # Move node i from A to ∅_i
                jumpNode = newA.pop(nodeIndex)
                nullSets[i].insert(0,jumpNode)
                print('Node', jumpNode, 'in network N has abandoned its network!')
                
    # Extracting networks from empty sets
    singularNetworks = [network for network in nullSets.values() if network]
    
    # Printing final configuration of networks
    print('--- Final state of networks ---')
    print('Final network N: ', newA)
    print('Final network M: ', sorted(newB))
    print('Final empty sets: ', singularNetworks)

    # Retuning the networks re-paritioned
    return newA,sorted(newB),*singularNetworks

# Testing function on example test networks
networkPartition([N,M],emptySets,systemTrust,nodeSecurity, networkSecurity)

# Note: Information that was not used and was removed from the function
# trustOfMinM = trustMatrix[len(N):len(N) + len(M), len(N):len(N) + len(M)]
# trustJinN = r(trustOfMinN) # {r_l(N),r_m(N)}
# trustJinM = r(trustOfMinM) # {r_l(M),r_m(M)}
# trustNinI = r(trustOfNinN, False) # {r_N(i),r_N(j),r_N(k)}
# trustNinJ = r(trustOfNinM, False) # {r_N(l),r_N(m)}
# trustMinJ = r(trustOfMinM, False) # {r_M(l),r_M(m)}

    
# %% Generalizing the algorithm iteratively - コンプリート

# Generalizing it to allow all nodes in all networks to jump
def generalPartition(networks, videSets, trustMatrix, nodesSecurity, networksSecurity):
    
    # Initializing copies of input data
    A,B = [network for network in networks]
    newA,newB = A.copy(),B.copy()
    nullSets = copy.deepcopy(videSets)
    
    # Printing initial configuration of networks 
    print('--- Original state of networks ---')
    print('Initial network N: ', A)
    print('Initial network M: ', B)
    print('Initial empty sets: ', nullSets)
    
    # Extracting trust block matrices from total trust matrix
    trustAinA = trustMatrix[:len(A), :len(A)]
    trustBinB = trustMatrix[len(A):len(A) + len(B), len(A):len(A) + len(B)]
    trustAinB = trustMatrix[:len(A), len(A):len(A) + len(B)]
    trustBinA = trustMatrix[len(A):len(A) + len(B), :len(A)]
    
    # Computing node-wide trust values for all i,j in A,B
    trustIinA = r(trustAinA)  # {r_i(A), r_j(A), r_k(A)}
    trustIinB = r(trustAinB)  # {r_i(B), r_j(B), r_k(B)}
    trustJinA = r(trustBinA)  # {r_l(A), r_m(A)}
    trustJinB = r(trustBinB)  # {r_l(B), r_m(B)}
    
    # Computing network-wide trust values
    trustAinJ = r(trustAinB, False)  # {r_A(l), r_A(m)}
    trustBinI = r(trustBinA, False)  # {r_B(i), r_B(j), r_B(k)}

    # Computing optimal locations for all nodes i,j in A,B
    jumpLocationsI = [[trustIinA[i], trustIinB[i]] for i in range(len(A))]
    jumpLocationsJ = [[trustJinA[j], trustJinB[j]] for j in range(len(B))]
    optimalLocationsI = [loc.index(min(loc)) for loc in jumpLocationsI]
    optimalLocationsJ = [loc.index(min(loc)) for loc in jumpLocationsJ]
    print('Optimal location for nodes i in N: ', optimalLocationsI)
    print('Optimal location for nodes j in M: ', optimalLocationsJ)
    
    # Performing jumps if optimal location network accepts
    for i in A:
        
        # Extracting the index of node i
        nodeIndex = A.index(i)
        
        # Selecting optimal location for node i in A
        location = optimalLocationsI[nodeIndex] #0 for A, 1 for B
        
        # Non-trivial location condition
        if location != 0:
            print('Node', A[nodeIndex], 'in network N wants to jump to network M.')
            
            # Seeing validity of trust condition
            if trustBinI[nodeIndex] <= networksSecurity[location]:
                
                # Move node i from A to B
                jumpNode = newA.pop(newA.index(i))
                newB.insert(len(newB), jumpNode)
                print('Node', A[nodeIndex], 'has jumped to network M!')  
                          
    for j in B:
        
        # Only looking at nodes which were originally there
        if j in newB:
        
            # Extracting the index of node j
            nodeIndex = B.index(j)
            
            # Selecting optimal location for node j in B
            location = optimalLocationsJ[nodeIndex]
                
            # Non-trivial location condition
            if location != 1:
                print('Node', B[nodeIndex], 'in network M wants to jump to network N.')
                
                # Seeing validity of trust condition
                if trustAinJ[nodeIndex] <= networksSecurity[location]:
                    
                    # Move node j from B to A
                    jumpNode = newB.pop(newB.index(j))
                    newA.insert(len(newA), jumpNode)
                    print('Node', B[nodeIndex], 'has jumped to network N!')

    # Seeing if nodes want to leave their own network into an empty set
    for i in A:
        
        # Only looking at nodes which were originally there
        if i in newA:
            
            # Extracting the index of node i
            nodeIndex = newA.index(i)
            
            # Seeing validity of trust conditions
            if trustIinA[nodeIndex] > nodesSecurity[i]:
                
                # Move node i from A to ∅_i
                jumpNode = newA.pop(nodeIndex)
                nullSets[i].insert(0,jumpNode)
                print('Node', i, 'in network N has abandoned its network!')
                
    for j in B:
        
        # Only looking at nodes which were originally there
        if j in newB:
            
            # Extracting the index of node j
            nodeIndex = newB.index(j)
            
            # Seeing validity of trust conditions
            if trustJinB[nodeIndex] > nodesSecurity[j]:
                
                # Move node j from B to ∅_j
                jumpNode = newB.pop(nodeIndex)
                nullSets[j].insert(0,jumpNode)
                print('Node', j, 'in network M has abandoned its network!')
    
    # Printing final configuration of networks
    print('--- Final state of networks ---')
    print('Final network N: ', sorted(newA))
    print('Final network M: ', sorted(newB))
    print('Final empty sets: ', nullSets)
    
    # Retuning the input repartitioned
    return [sorted(newA), sorted(newB)], nullSets, trustMatrix, nodesSecurity, networksSecurity  

# Testing function on example test networks
generalPartition([N, M], emptySets, systemTrust, nodeSecurity, networkSecurity)[:2]

# Note: Information that was not used and was removed from the function
# trustNinI = r(trustOfNinN, False)  # {r_N(i), r_N(j), r_N(k)}
# trustMinJ = r(trustOfMinM, False)  # {r_M(l), r_M(m)}


#%% Testing the iterative capability of this function - コンプリート

# Initializing the amount of iterations
totalIterations = 3

# Initializing the function input
functionInput = ([N, M], emptySets, systemTrust, nodeSecurity, networkSecurity)

# Iteratively calling the partitioning function
for iteration in range(totalIterations):
    print('Iteration:',iteration+1)
    functionInput = generalPartition(*functionInput)


# %% Testing the above functions with KNOWN examples  - コンプリート

###### Case i) All abandon: i,j,k,l,m -> 0
securityN = {0:0,1:0,2:0}
securityM = {3:0,4:0}
nodeSecurity = securityN | securityM
orderedSecurityN = sorted(list(securityN.values()))
orderedSecurityM = sorted(list(securityM.values()))
securityNetworkN = np.max(orderedSecurityN[int(len(orderedSecurityN)/2):])
securityNetworkM = np.max(orderedSecurityM[int(len(orderedSecurityM)/2):])
networkSecurity = {0:securityNetworkN,1:securityNetworkM}
print('---- Case i) All abandon ---')
print(
    generalPartition([N, M], emptySets, systemTrust, nodeSecurity, networkSecurity)[:2]
)

###### Case ii) All swap: i,j,k -> M, l,m -> N
trustNinN = np.array([
    [0,1/2,1/4],
    [1/3,0,1/4],
    [1/2,1,0]
])
trustMinM = np.array([
    [0,1/4],
    [1/3,0]
])
trustNinM = np.array([
    [0,0],
    [0,0],
    [0,0]
])
trustMinN = np.array([
    [0,0,0],
    [0,0,0]
])
systemTrust = np.hstack((
    np.vstack((trustNinN,trustMinN)), np.vstack((trustNinM,trustMinM))
))
securityN = {0:1/6,1:1/2,2:1/3}
securityM = {3:1/2,4:1/4}
nodeSecurity = securityN | securityM
orderedSecurityN = sorted(list(securityN.values()))
orderedSecurityM = sorted(list(securityM.values()))
securityNetworkN = np.max(orderedSecurityN[int(len(orderedSecurityN)/2):])
securityNetworkM = np.max(orderedSecurityM[int(len(orderedSecurityM)/2):])
networkSecurity = {0:securityNetworkN,1:securityNetworkM}
print('---- Case ii) All swap ---')
print(
    generalPartition([N, M], emptySets, systemTrust, nodeSecurity, networkSecurity)[:2]
)

###### Case iii) Unified network: i,j,k -> M, l,m -> M
trustNinN = np.array([
    [6,1/2,1/4],
    [1/3,0,1/4],
    [1/2,1,6]
])
trustMinM = np.array([
    [0,0],
    [0,0]
])
trustNinM = np.array([
    [0,0],
    [0,0],
    [0,0]
])
trustMinN = np.array([
    [1/6,1/6,1/6],
    [1/6,1/6,1/6]
])
systemTrust = np.hstack((
    np.vstack((trustNinN,trustMinN)), np.vstack((trustNinM,trustMinM))
))
securityN = {0:1/60,1:1/20,2:1/30}
securityM = {3:1/2,4:1/4}
nodeSecurity = securityN | securityM
orderedSecurityN = sorted(list(securityN.values()))
orderedSecurityM = sorted(list(securityM.values()))
securityNetworkN = np.max(orderedSecurityN[int(len(orderedSecurityN)/2):])
securityNetworkM = np.max(orderedSecurityM[int(len(orderedSecurityM)/2):])
networkSecurity = {0:securityNetworkN,1:securityNetworkM}
print('---- Case iii) Unified network ---')
print(
    generalPartition([N, M], emptySets, systemTrust, nodeSecurity, networkSecurity)[:2]
)


# %% NEXT STEPS: 
# - Generalize to arbitrary amount of networks [Hans suggestion; work with list elements instead of calling them N,...,M = [...]]
# [[Generalize to have second choices]]

