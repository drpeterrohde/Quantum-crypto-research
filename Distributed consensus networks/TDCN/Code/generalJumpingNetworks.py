#%% Importing modules - コンプリート

import numpy as np


# %% Defining the networks, their trust, and their security - コンプリート

# Defining the networks and their elements
N = [0,1,2] # Network N with nodes: i,j,k = 0,1,2
M = [3,4] # Network M with nodes: l,m = 3,4

# Defining node-respective empty sets
emptySets = {k:[] for k in range(len(N)+len(M))}

# Defining all trust matrix permutations
trustNinN = np.array([
    [0,1/2,1/4],
    [1/3,0,1/4],
    [1/2,1,0]
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
trustMinM = np.array([
    [0,1/4],
    [1/3,0]
])

# Combining trust matrices into one total one
systemTrust = np.hstack((
    np.vstack((trustNinN,trustMinN)), np.vstack((trustNinM,trustMinM))
))

# Defining the security parameters of the nodes in the network
securityN = {0:1/6,1:1/2,2:1/3}
securityM = {3:1/2,4:1/4}
nodeSecurity = securityN | securityM

# Defining the network wide security parameters via most lenient n/2 nodes
orderedSecurityN = sorted(list(securityN.values()))
orderedSecurityM = sorted(list(securityM.values()))
securityNetworkN = np.max(orderedSecurityN[int(len(orderedSecurityN)/2):])
securityNetworkM = np.max(orderedSecurityM[int(len(orderedSecurityM)/2):])
networkSecurity = {0:securityNetworkN,1:securityNetworkM}

# Printing the outcome of definitions
print('Trust of network N in itself:')
print(trustNinN)
print('Trust of network N in M:')
print(trustNinM)
print('Trust of network M in N:')
print(trustMinN)
print('Trust of network M in itself:')
print(trustMinM)
print('System trust matrix:')
print(systemTrust)
print('Possible empty sets:')
print(emptySets)
print('Security parameters nodes:')
print(nodeSecurity)
print('Security parameters networks:')
print(networkSecurity)


# %% Defining the trust functions at different scales - コンプリート

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
print('Trusts of nodes in their own network:')
print(r(trustNinN))
print('Trust of a network in its nodes:')
print(r(trustNinN,False))
print('Security parameters of nodes in network N:')
print(securityN)
print('Security parameters of network N:')
print(securityNetworkN)
print('--- Boolean decision outcome ---')
print('Node wide decisions:')
print(f(trustNinN, securityN, securityNetworkN))
print('Network wide decisions:')
print(f(trustNinN, securityN, securityNetworkN, False))
print('--- Trust between different networks ---')
print('Trust of network N in network M:')
print(rr(trustNinM,trustMinN))
print('Trust of network M in network N:')
print(rr(trustNinM,trustMinN,False))

# %% Pre-Generalization: Practicing trust block matrix extraction for N=3

# List cutting practice
listeroni = ['a','b','c','d','e','f','g']
# Observation!:
# Normal cutting: listeroni[start:stop], start <= x < stop. Starts at x=0.
print('Test cut: ', listeroni[2:4+1]) #Start at x=2 'c' to x=4 'e'

# Trust array matrix for 3 networks
testMatrix = np.array([
    ['ii','ij','ik','il','im','in'],
    ['ji','jj','jk','jl','jm','jn'],
    ['ki','kj','kk','kl','km','kn'],
    ['li','lj','lk','ll','lm','ln'],
    ['mi','mj','mk','ml','mm','mn'],
    ['ni','nj','nk','nl','nm','nn']
])

# Network sizes
size1 = 3
size2 = 2
size3 = 1

# Diagonal block matrices
alphaMatrix = testMatrix[0:2+1,
                         0:2+1]
print('Alpha Matrix \n', alphaMatrix)
betaMatrix = testMatrix[3:4+1,
                        3:4+1]
print('Beta Matrix \n', betaMatrix)
gammaMatrix = testMatrix[5:,5:]
print('Gamma Matrix \n', gammaMatrix)

# Off-diagonal block matrices
sigmaMatrix = testMatrix[0:2+1, #Trust M in N
                         3:4+1]
print('Sigma Matrix: \n', sigmaMatrix)
lambdaMatrix = testMatrix[3:4+1, #Trust N in M
                         0:2+1]
print('Lambda Matrix: \n', lambdaMatrix)
muMatrix = testMatrix[0:2+1, #Trust N in P
                     5:]
print('Mu Matrix: \n', muMatrix)
nuMatrix = testMatrix[5:, #Trust P in N
                     0:2+1]
print('Nu Matrix: \n', nuMatrix)
thetaMatrix = testMatrix[3:4+1, #Trust M in P
                     5:]
print('Theta Matrix: \n', thetaMatrix)
rhoMatrix = testMatrix[5:, #Trust P in M
                     3:4+1]
print('Rho Matrix: \n', rhoMatrix)

# Trying but with sizes only when cutting! [Automatic]

# Diagonal block matrices
newAlphaMatrix = testMatrix[:size1,
                         :size1]
print('New Alpha Matrix Test: ', np.array_equal(alphaMatrix,newAlphaMatrix))
newBetaMatrix = testMatrix[size1:size1+size2,
                        size1:size1+size2]
print('New Beta Matrix Test: ', np.array_equal(betaMatrix,newBetaMatrix))
newGammaMatrix = testMatrix[size1+size2:size1+size2+size3,
                         size1+size2:size1+size2+size3]
print('New Gamma Matrix Test: ', np.array_equal(gammaMatrix,newGammaMatrix))
# Observation!:
# For n-th matrix, we want to do:
# \sum_i=1^n-1 size_i : \sum_i=1^n size_i

# Off-diagonal block matrices
# newSigmaMatrix = testMatrix[]

# Testing autonomous cutting algorithm on N=3 index example
sizesList = [size1,size2,size3]
sizer = len(sizesList)
blockMatrices = []
A = lambda alpha: sum(sizesList[i] for i in range(alpha))

for i in range(sizer):
    for j in range(sizer):
        blockMatrices.append(testMatrix[A(i):A(i+1),A(j):A(j+1)])
#Outputs going along horizontal
#blockMatrices : trustNinN, trustNinM, trustNinP, trustMinN, trustMinM, trustMinP, trustPinN, trustPinM, trustPinP

# %% Generalizing the paritioning function to arbitrary networks: Reproducing N=2 ----

# Defining networks and empty sets
networks = [N,M]
networkNames = ['N','M']
networksCopy = [j.copy() for j in networks]
networkSizes = [len(i) for i in networks]
numberOfNetworks = len(networkSizes)

# Printing intial configuration of networks 
print('--- Original state of networks ---')
for i in range(len(networks)):
    print('Initial network',i,':', networks[i])
print('Initial empty sets: ', emptySets)


# %% - Extracting the trust block matrices

# Defining the summation equation for block matrices
A = lambda alpha: sum(networkSizes[i] for i in range(alpha))

# Extracting the block matrices from system trust
blockMatrices = []

# Populating the block matrix array with block matrices
for i in range(numberOfNetworks):
    for j in range(numberOfNetworks):
        blockMatrices.append(systemTrust[A(i):A(i+1),A(j):A(j+1)])
        

# %% - Computing trust sums of network trust block matrices

# Computing the trust sums from the perspectives of the nodes
nodeSums = []
for i in blockMatrices:
    nodeSums.append(r(i))
# N = 3 Output: trustIinN, trustIinM, trustIinP, trustJinN, trustJinM, trustJinP, trustKinN, trustKinM, trustKinP
# N = 2 Output: trustIinN, trustIinM,  trustJinN, trustJinM 
    
# Computing the trust sums from the perspectives of the networks
networkSums = []
for i in blockMatrices:
    networkSums.append(r(i,False))
# N = 3 Output: trustNinI, trustNinJ, trustNinP, trustMinI, trustMinJ, trustMinP, trustPinI, trustPinJ, trustPinK
# N = 2 Output: trustNinI, trustNinJ, trustMinI, trustMinJ


# %% - Computing jump locations of nodes

# Optimal jump locations for the network nodes
optimalLocations = []

# Iterating through the network to compute optimal jump locations
for n in range(len(networks)):
    
    # Printing the information of the current network
    print('Network:', n)
    networkLength = len(networks[n])
    print('Network length:', networkLength)
    targetTrusts = nodeSums[n*len(networks):(n+1)*len(networks)]
    
    # Initializing jump locations for nodes in network n
    jumpLocations = []
    
    # Iterating through the nodes of the networks
    for i in range(networkLength):
        for j in targetTrusts:
            jumpLocations.append(j[i])

    # Making them into q-plets
    pletFormer = lambda lst, q: [lst[i:i + q] for i in range(0, len(lst), q)]
    orderedLocations = pletFormer(jumpLocations,numberOfNetworks)
    print('Ordered locations:',orderedLocations)
    
    # Computing optimal locations
    optimalLocationsTemp = [loc.index(min(loc)) for loc in orderedLocations]
    print('Optimal locations:', optimalLocationsTemp)
    optimalLocations.append(optimalLocationsTemp)

# Returning complete list of optimal locations for all nodes in each network
print('Full optimal locations:', optimalLocations)


# %% Performing jumps for every network
for n in range(len(networks)):
    
    # Printing configuration of the current network
    currentNetwork = networks[n]
    currentCopy = networksCopy[n]
    currentOptimal = optimalLocations[n]
    print('Network',networkNames[n],':', currentNetwork)
    print('Network copy', networkNames[n],':', sorted(currentCopy))
    print('Network optimal locations:', currentOptimal)
    
    # Defining external networks trusts in this one
    externalTrusts = []
    trustExtractor = lambda lst, q: [[lst[i] for i in range(start, len(lst), q)] for start in range(q)]
    externalTrusts = trustExtractor(networkSums,numberOfNetworks)[n]
    
    # Iterating through the nodes of the networks
    for i in currentNetwork:

        # Only looking at nodes originally in network
        if i in currentCopy:
            
            # Extracting the index of node i
            nodeIndex = currentNetwork.index(i)
            
            # Selecting optimal location for node i in network n
            location = currentOptimal[nodeIndex]
            locationNetwork = networksCopy[location]

            # Non-trivial location condition
            if location != n:
                print('Node', currentNetwork[nodeIndex], 'in network', networkNames[n], 'wants to jump network',networkNames[location],'!')
                
                # Seeing validity of trust condition [in function this should be networksSecurity]
                if externalTrusts[location][nodeIndex] <= networkSecurity[location]:
                    
                    # Move node from one network to another
                    jumpNode = currentCopy.pop(currentCopy.index(i))
                    locationNetwork.insert(len(locationNetwork), jumpNode)
                    print('Node', currentNetwork[nodeIndex], 'has jumped to network',networkNames[location],'!')
                                    
print('Networks after jumping events:', networksCopy)  

# After abandoning, the networks will be sorted with
# [sorted(sublist) for sublist in lst]


# %% Performing abandons for every network
for n in range(len(networks)):
    
    # Printing configuration of the current network
    currentNetwork = networks[n]
    currentCopy = networksCopy[n]
    print('Network',networkNames[n],':', currentNetwork)
    print('Network copy', networkNames[n],':', sorted(currentCopy))

    # Defining the trusts of nodes in their own network
    internalTrusts = nodeSums[n*(numberOfNetworks+1)]
    
    # Iterating through the nodes of the networks
    for i in currentNetwork:
        
        # Only looking at nodes originally in the network
        if i in currentCopy:
            
            # Extracting the index of node i
            nodeIndex = currentNetwork.index(i)
            
            # Seeing validity of trust conditions [in function this should be nodesSecurity]
            if internalTrusts[nodeIndex] > nodeSecurity[i]:
                
                # Move node i to ∅_i
                jumpNode = currentCopy.pop(currentCopy.index(i))
                emptySets[i].insert(0,jumpNode)
                print('Node', i, 'in network', networkNames[n], 'has abandoned its network!')

print('Networks after abandon events:', networksCopy) 
print('Emtpy sets after evolution:', emptySets)


# %% Creating new networks from old ones

# Reallocating empty sets as new networks
reallocateNetworks = lambda nets, empties: (
    [[i] for i in sorted(sum(empties.values(), []) + sum(nets, []))[:2]] + [sorted(sum(empties.values(), []) + sum(nets, []))[2:]],
    {k: [] for k in empties}
)

# Updating the new networks 
newNetworks, newEmptySets = reallocateNetworks(networksCopy, emptySets)
print('Updated networks:', newNetworks)
print('Updated emtpy sets:', newEmptySets)


# %%
