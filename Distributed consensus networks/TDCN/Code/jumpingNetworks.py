#%% Importing modules - コンプリート

# Standard mathematics modules
import numpy as np
import copy
import matplotlib.pyplot as plt                  

# Standard debugging matrix
debugMatrix = np.array([
    [1,2],
    [3,4]
    ])


# %% Defining the different networks, trust matrices, and parameters - コンプリート

# Defining the network elements
networkN = [0,1,2] # i,j,k
networkM = [3,4] # l,m

# Defining node-respective empty sets
emptySets = {0:[],1:[],2:[],3:[],4:[]}

# Defining trust matrices betwixt both networks
trustNinN = np.array([
    [0,1/2,1/4],[1/3,0,1/4],[1/2,1,0]
])
trustMinM = np.array([
    [0,1/4],[1/3,0]
])
trustNinM = np.array([
    [1,1/5],[1/3,1/2],[1/3,1]
])
trustMinN = np.array([
    [1/7,1/2,1/3],[1,1/4,1/2]
])

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

# Combining trust matrices into one total one
totalTrust = np.hstack((
    np.vstack((trustNinN,trustMinN)), np.vstack((trustNinM,trustMinM))
))

# Printing the outcome of manipulation
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

# Testing the functions on different networks
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


# %% Defining the re-paritioning algorithm: Algorithm 2 - コンプリート

# Defining the function which repartitions a group of networks [only N can jump currently]
def networkPartition(networks,trustMatrix, nodeSecurity, networkSecurity, videSets):
    
    # Initializing network copies
    originalN, originalM = [subnetwork for subnetwork in networks]
    N, M = originalN.copy(), originalM.copy()
    
    # Printing intial configuration of networks 
    print('--- Original state of networks ---')
    print('Initial network N: ', N)
    print('Initial network M: ', M)
    print('Initial empty sets: ', emptySets)
    
    # Extracting trust block matrices from total trust matrix
    trustOfNinN = trustMatrix[:len(N), :len(N)]
    trustOfMinM = trustMatrix[len(N):len(N) + len(M), len(N):len(N) + len(M)]
    trustOfNinM = trustMatrix[:len(N), len(N):len(N) + len(M)]
    trustOfMinN = trustMatrix[len(N):len(N) + len(M), :len(N)]
    
    # Copying the possible empty sets allowed
    nullSets = copy.deepcopy(videSets)
    
    # Computing node wide trust values (i \in N, j \in M)
    trustIinN = r(trustOfNinN) # {r_i(N),r_j(N),r_k(N)}
    trustIinM = r(trustOfNinM) # {r_i(M),r_j(M),r_k(M)}
    trustJinN = r(trustOfMinN) # {r_l(N),r_m(N)}
    trustJinM = r(trustOfMinM) # {r_l(M),r_m(M)}
    
    # Computing network wide trust values
    trustNinI = r(trustOfNinN, False) # {r_N(i),r_N(j),r_N(k)}
    trustNinJ = r(trustOfNinM, False) # {r_N(l),r_N(m)}
    trustMinI = r(trustOfMinN, False) # {r_M(i),r_M(j),r_M(k)}
    trustMinJ = r(trustOfMinM, False) # {r_M(l),r_M(m)}

    # Computing optimal locations for all nodes i \in N
    jumpLocations = [[trustIinN[i],trustIinM[i]] for i in N]
    optimalLocations = [set.index(np.min(set))for set in jumpLocations]
    
    # Performing jumps if optimal location network accepts
    for i in range(len(N)):
        location = optimalLocations[i]
        if location != 0:
            if trustMinI[i] <= networkSecurity[location]:
                M.insert(0,N.pop(i))
    
    # Seeing if nodes want to leave their own network into an empty set
    for i in range(len(N)):
        location = optimalLocations[i]
        if trustIinN[i] > nodeSecurity[i]:
            nullSets[i].insert(0,N.pop(i))
                
    # If empty sets have been populated, make new networks
    singularNetworks = [network for network in nullSets.values() if network]
    
    # Flattening the empty networks
    flattenedSingularNetworks = [network for sublist in singularNetworks for network in sublist]
    
    # Printing final configuration of networks
    print('--- Final state of networks ---')
    print('Final network N: ', N)
    print('Final network M: ', M)
    print('Final empty sets: ', singularNetworks)
    
    
    return N,M,flattenedSingularNetworks
    
# Testing function on example test networks
networkPartition([networkN,networkM],totalTrust,securityNM, securityNetworks,emptySets)
    
    
# %% Generalizing the algorithm iteratively - コンプリート

# i) Generalizing it to allow all nodes in all networks to jump
def generalPartition(networks, trustMatrix, nodeSecurity, networkSecurity, videSets):
    
    # Initializing network copies
    originalN, originalM = [subnetwork for subnetwork in networks]
    N, M = originalN.copy(), originalM.copy()
    
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
    
    # Copying the possible empty sets allowed
    nullSets = {k: [] for k in videSets.keys()}
    
    # Computing node-wide trust values (i \in N, j \in M)
    trustIinN = r(trustOfNinN)  # {r_i(N), r_j(N), r_k(N)}
    trustIinM = r(trustOfNinM)  # {r_i(M), r_j(M), r_k(M)}
    trustJinN = r(trustOfMinN)  # {r_l(N), r_m(N)}
    trustJinM = r(trustOfMinM)  # {r_l(M), r_m(M)}
    
    # Computing network-wide trust values
    trustNinI = r(trustOfNinN, False)  # {r_N(i), r_N(j), r_N(k)}
    trustNinJ = r(trustOfNinM, False)  # {r_N(l), r_N(m)}
    trustMinI = r(trustOfMinN, False)  # {r_M(i), r_M(j), r_M(k)}
    trustMinJ = r(trustOfMinM, False)  # {r_M(l), r_M(m)}

    # Computing optimal locations for all nodes i \in N, and j \in M
    jumpLocationsI = [[trustIinN[i], trustIinM[i]] for i in range(len(N))]
    jumpLocationsJ = [[trustJinN[j], trustJinM[j]] for j in range(len(M))]
    
    optimalLocationsI = [loc.index(min(loc)) for loc in jumpLocationsI]
    optimalLocationsJ = [loc.index(min(loc)) for loc in jumpLocationsJ]
    
    # Performing jumps if optimal location network accepts
    for i in range(len(N)):
        location = optimalLocationsI[i]
        if location != 0:
            if trustMinI[i] <= networkSecurity[location]:
                M.insert(0, N.pop(i))
    for j in range(len(M)):
        if j < len(optimalLocationsJ): # Check if j is within the range of optimalLocationsJ
            location = optimalLocationsJ[j]
            if location != 0:
                if trustNinJ[j] <= networkSecurity[location]:
                    N.insert(0, M.pop(j))
    
    # Seeing if nodes want to leave their own network into an empty set
    for i in range(len(N)):
        location = optimalLocationsI[i]
        if trustIinN[i] > nodeSecurity[i]:
            nullSets[N[i]].insert(0, N.pop(i))
    for j in range(len(M)):
        if j < len(optimalLocationsJ): # Check if j is within the range of optimalLocationsJ
            location = optimalLocationsJ[j]
            if trustJinM[j] > nodeSecurity[j]:
                nullSets[M[j]].insert(0, M.pop(j))
                
    # If empty sets have been populated, make new networks
    singularNetworks = [network for network in nullSets.values() if network]
    
    # Flattening the empty networks
    flattenedSingularNetworks = [network for sublist in singularNetworks for network in sublist]
    
    # Printing final configuration of networks
    print('--- Final state of networks ---')
    print('Final network N: ', N)
    print('Final network M: ', M)
    print('Final empty sets: ', singularNetworks)
    
    return N, M, flattenedSingularNetworks

# Testing function on example test networks
generalPartition([networkN, networkM], totalTrust, securityNM, securityNetworks, emptySets)


# %%
