#%% Importing modules - コンプリート

# Standard mathematics modules
import numpy as np


# %% Defining the networks, trust, and security parameters - コンプリート

# Defining the network and its elements
networkN = [0,1,2] # Nodes: i,j,k
networkM = [3,4] # Nodes: l,m

# Defining node-respective empty sets
emptySets = {0:[],1:[],2:[],3:[],4:[]}

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
totalTrust = np.hstack((
    np.vstack((trustNinN,trustMinN)), np.vstack((trustNinM,trustMinM))
))

# Defining the security parameters of the nodes in the network
securityN = {0:1/6,1:1/2,2:1/3}
securityM = {3:1/2,4:1/4}
securityNM = securityN | securityM

# Defining the network wide security parameters via most lenient n/2
orderedSecurityN = sorted(list(securityN.values()))
orderedSecurityM = sorted(list(securityM.values()))
securityNetworkN = np.max(orderedSecurityN[int(len(orderedSecurityN)/2):])
securityNetworkM = np.max(orderedSecurityM[int(len(orderedSecurityM)/2):])
securityNetworks = {0:securityNetworkN,1:securityNetworkM}

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
print(totalTrust)
print('Possible empty sets')
print(emptySets)
print('Security parameters nodes')
print(securityNM)
print('Security parameters networks')
print(securityNetworks)


# %% Defining the different scale trust functions - コンプリート

# Defining the trust function between nodes and networks
def r(trustAinA, forward=True):
    
    # Computing the trust sum for all nodes i for r_i(A)
    if forward == True:
        
        # Initializing the network and empty trust values
        networkSize = len(trustAinA)
        trustSum = np.zeros(networkSize)
        for i in range(networkSize):
            trustSum[i] =  1/(networkSize) * np.sum(trustAinA[i])
             
    # Computing the trust sum for all nodes i for r_A(i)
    if forward == False:
        
        # Initializing the network and empty trust values
        networkSize = len(trustAinA.T)
        trustSum = np.zeros(networkSize)
        for i in range(networkSize):
            trustSum[i] =  1/(networkSize) * np.sum(trustAinA.T[i])
    
    return trustSum

# Defining the trust function between networks   
def rr(trustAinB, trustBinA, forward=True):
    
    # Computing the individual trusts amongst the networks
    firstNetworkTrusts = r(trustAinB)
    secondNetworkTrusts = r(trustBinA)
    
    # Computing the trust between networks for r(A,B)
    if forward == True:
        totalNetworkTrust = np.max(firstNetworkTrusts)
    
    # Computing the trust between networks for r(B,A)
    if forward == False:
        totalNetworkTrust = np.max(secondNetworkTrusts)
        
    return totalNetworkTrust

# Defining the boolean decision function between nodes and networks
def f(trustAinA, nodeSecurity, networkSecurity, forward=True):
    
    # Computing the size and individual trusts among the network
    networkSize = len(trustAinA)
    trustIinA = r(trustAinA)
    trustAinI = r(trustAinA, False)
    
    # Initializing empty array of boolean values
    booleanArray = np.zeros(networkSize)
    
    # Computing the booleans for r_i(A) based on parameters
    if forward == True:
        for i in range(networkSize):
            if trustIinA[i] <= nodeSecurity[i]:
                booleanArray[i] = 1
             
    # Computing the booleans for r_A(i) based on parameters
    if forward == False:
        for i in range(networkSize):
            if trustAinI[i] <= networkSecurity:
                booleanArray[i] = 1
            
    return booleanArray

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
def networkPartition(networks,trustMatrix, nodeSecurity, networkSecurity, videSets):
    
    # Initializing copies of input data
    originalN, originalM = [subnetwork for subnetwork in networks]
    N, M = originalN.copy(), originalM.copy()
    nullSets = {k: [] for k in videSets.keys()}
    
    # Printing intial configuration of networks 
    print('--- Original state of networks ---')
    print('Initial network N: ', N)
    print('Initial network M: ', M)
    print('Initial empty sets: ', nullSets)
    
    # Extracting block trust matrices from total trust matrix
    trustOfNinN = trustMatrix[:len(N), :len(N)]
    trustOfNinM = trustMatrix[:len(N), len(N):len(N) + len(M)]
    trustOfMinN = trustMatrix[len(N):len(N) + len(M), :len(N)]
    
    # Computing node wide trust values for all nodes i \in N
    trustIinN = r(trustOfNinN) # {r_i(N),r_j(N),r_k(N)}
    trustIinM = r(trustOfNinM) # {r_i(M),r_j(M),r_k(M)}
    
    # Computing network wide trust values
    trustMinI = r(trustOfMinN, False) # {r_M(i),r_M(j),r_M(k)}
    
    # Computing optimal locations for all nodes i \in N
    jumpLocations = [[trustIinN[i], trustIinM[i]] for i in range(len(N))]
    optimalLocations = [loc.index(min(loc)) for loc in jumpLocations]
    
    # Performing jumps if optimal location network accepts
    for i in range(len(networkN)):
        location = optimalLocations[i]
        if location != 0:
            print('Node', i, 'wants to jump.')
            if trustMinI[i] <= networkSecurity[location]:
                M.insert(0, N.pop(i))
                print('Node', networkN[i], 'has jumped to network M!')
    
    # Seeing if nodes want to leave their own network into an empty set
    for i in range(len(networkN)):
        if networkN[i] in N:
            if trustIinN[i] > nodeSecurity[networkN[i]]:
                nullSets[networkN[i]].insert(0,N.pop(N.index(networkN[i])))
                print('Node', networkN[i], 'has abandoned its network!')
                
    # If empty sets have been populated, make new networks
    singularNetworks = [network for network in nullSets.values() if network]
    
    # Printing final configuration of networks
    print('--- Final state of networks ---')
    print('Final network N: ', N)
    print('Final network M: ', M)
    print('Final empty sets: ', singularNetworks)

    # Retuning the networks re-paritioned
    return N,M,*singularNetworks

# Testing function on example test networks
networkPartition([networkN,networkM],totalTrust,securityNM, securityNetworks,emptySets)

# Note: Information that was not used and was removed from the function
# trustOfMinM = trustMatrix[len(N):len(N) + len(M), len(N):len(N) + len(M)]
# trustJinN = r(trustOfMinN) # {r_l(N),r_m(N)}
# trustJinM = r(trustOfMinM) # {r_l(M),r_m(M)}
# trustNinI = r(trustOfNinN, False) # {r_N(i),r_N(j),r_N(k)}
# trustNinJ = r(trustOfNinM, False) # {r_N(l),r_N(m)}
# trustMinJ = r(trustOfMinM, False) # {r_M(l),r_M(m)}

    
# %% Generalizing the algorithm iteratively - コンプリート

# i) Generalizing it to allow all nodes in all networks to jump
def generalPartition(networks, trustMatrix, nodeSecurity, networkSecurity, videSets):
    
    # Initializing copies of input data
    originalN, originalM = [subnetwork for subnetwork in networks]
    N, M = originalN.copy(), originalM.copy()
    nullSets = {k: [] for k in videSets.keys()}
    
    # Printing initial configuration of networks 
    print('--- Original state of networks ---')
    print('Initial network N: ', N)
    print('Initial network M: ', M)
    print('Initial empty sets: ', videSets)
    
    # Extracting trust block matrices from total trust matrix
    trustOfNinN = trustMatrix[:len(N), :len(N)]
    trustOfMinM = trustMatrix[len(N):len(N) + len(M), len(N):len(N) + len(M)]
    trustOfNinM = trustMatrix[:len(N), len(N):len(N) + len(M)]
    trustOfMinN = trustMatrix[len(N):len(N) + len(M), :len(N)]
    
    # Computing node-wide trust values (i \in N, j \in M)
    trustIinN = r(trustOfNinN)  # {r_i(N), r_j(N), r_k(N)}
    trustIinM = r(trustOfNinM)  # {r_i(M), r_j(M), r_k(M)}
    trustJinN = r(trustOfMinN)  # {r_l(N), r_m(N)}
    trustJinM = r(trustOfMinM)  # {r_l(M), r_m(M)}
    
    # Computing network-wide trust values
    trustNinJ = r(trustOfNinM, False)  # {r_N(l), r_N(m)}
    trustMinI = r(trustOfMinN, False)  # {r_M(i), r_M(j), r_M(k)}

    # Computing optimal locations for all nodes i \in N, and j \in M
    jumpLocationsI = [[trustIinN[i], trustIinM[i]] for i in range(len(N))]
    jumpLocationsJ = [[trustJinN[j], trustJinM[j]] for j in range(len(M))]
    optimalLocationsI = [loc.index(min(loc)) for loc in jumpLocationsI]
    optimalLocationsJ = [loc.index(min(loc)) for loc in jumpLocationsJ]
    
    # Performing jumps if optimal location network accepts
    for i in range(len(networkN)):
        location = optimalLocationsI[i]
        if location != 0:
            print('Node', networkN[i], 'wants to jump.')
            if trustMinI[i] <= networkSecurity[location]:
                M.insert(0, N.pop(N[i])) ##########
                print('Node', networkN[i], 'has jumped to network M!')
    for j in range(len(networkM)):
        location = optimalLocationsJ[j]
        if location != 0:
            print('Node', networkM[j], 'wants to jump.')
            if trustNinJ[j] <= networkSecurity[location]:
                N.insert(0, M.pop(M[j])) #########
                print('Node', networkM[j], 'has jumped to network N!')

    # Seeing if nodes want to leave their own network into an empty set
    for i in range(len(networkN)):
        if networkN[i] in N:
            if trustIinN[i] > nodeSecurity[networkN[i]]:
                nullSets[networkN[i]].insert(0,N.pop(N.index(networkN[i])))
                print('Node', networkN[i], 'has abandoned its network!')
    for j in range(len(networkM)):
        if networkM[j] in M:
            if trustJinM[j] > nodeSecurity[networkM[j]]:
                nullSets[networkM[j]].insert(0,M.pop(M.index(networkM[j])))
                print('Node', networkM[j], 'has abandoned its network!')
                    
        # If empty sets have been populated, make new networks
        singularNetworks = [network for network in nullSets.values() if network]
    
    # Printing final configuration of networks
    print('--- Final state of networks ---')
    print('Final network N: ', N)
    print('Final network M: ', M)
    print('Final empty sets: ', singularNetworks)
    
    # Retuning the networks re-paritioned
    return N, M, *singularNetworks

# Testing function on example test networks
generalPartition([networkN, networkM], totalTrust, securityNM, securityNetworks, emptySets)

# Note: Information that was not used and was removed from the function
# trustNinI = r(trustOfNinN, False)  # {r_N(i), r_N(j), r_N(k)}
# trustMinJ = r(trustOfMinM, False)  # {r_M(l), r_M(m)}


# %% Testing the above functions with KNOWN examples  - コンプリート

###### Case i) All abandon: i,j,k,l,m -> 0
securityN = {0:0,1:0,2:0}
securityM = {3:0,4:0}
securityNM = securityN | securityM
orderedSecurityN = sorted(list(securityN.values()))
orderedSecurityM = sorted(list(securityM.values()))
securityNetworkN = np.max(orderedSecurityN[int(len(orderedSecurityN)/2):])
securityNetworkM = np.max(orderedSecurityM[int(len(orderedSecurityM)/2):])
securityNetworks = {0:securityNetworkN,1:securityNetworkM}
print('---- Case i) All abandon ---')
print(
    generalPartition([networkN, networkM], totalTrust, securityNM, securityNetworks, emptySets)
)

###### Case ii) All swap: i,j,k -> M, l,m -> N [[bug: pop index out of range]]
# # Defining all trust matrix permutations
# trustNinN = np.array([
#     [0,1/2,1/4],
#     [1/3,0,1/4],
#     [1/2,1,0]
# ])
# trustMinM = np.array([
#     [0,1/4],
#     [1/3,0]
# ])
# trustNinM = np.array([
#     [0,0],
#     [0,0],
#     [0,0]
# ])
# trustMinN = np.array([
#     [0,0,0],
#     [0,0,0]
# ])
# totalTrust = np.hstack((
#     np.vstack((trustNinN,trustMinN)), np.vstack((trustNinM,trustMinM))
# ))
# securityN = {0:1/6,1:1/2,2:1/3}
# securityM = {3:1/2,4:1/4}
# securityNM = securityN | securityM
# orderedSecurityN = sorted(list(securityN.values()))
# orderedSecurityM = sorted(list(securityM.values()))
# securityNetworkN = np.max(orderedSecurityN[int(len(orderedSecurityN)/2):])
# securityNetworkM = np.max(orderedSecurityM[int(len(orderedSecurityM)/2):])
# securityNetworks = {0:securityNetworkN,1:securityNetworkM}
# print('---- Case ii) All swap ---')
# print(
#     generalPartition([networkN, networkM], totalTrust, securityNM, securityNetworks, emptySets)
# )

###### Case iii) Unified network: i,j,k -> M, l,m -> M



# %% NEXT STEPS: 
# - Modify output to fit into input
# - Generalize to arbitrary amount of networks [Hans suggestion; work with list elements instead of calling them N,...,M = [...]]
# [Generalize to have second choices]

