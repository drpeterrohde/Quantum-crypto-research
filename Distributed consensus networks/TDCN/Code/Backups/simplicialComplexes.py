#%% Importing modules - コンプリート

# Standard mathematics modules
import numpy as np
import matplotlib.pyplot as plt                  

# Standard debugging matrix
debugMatrix = np.array([
    [1,2],
    [3,4]
    ])

#%% Defining the different trust functions - コンプリート

# Defining test trust matrices that represent r_ij normalized to 1
initialNetwork = np.array([#Trust of nodes within N
    [0,1/2,1/2], #r_ij
    [1/4,0,1],
    [1/4,1/3,0]
])
perspectiveNetwork = np.array([#Trust of nodes in N of nodes in N'
    [1/3,1/4,1/2], #r_ij'
    [1/4,1,1],
    [1/4,1/5,1/8]
])
reversedNetwork = np.array([#Trust of nodes in N' of nodes in N
    [1/7,1/2,1], #r_i'j
    [1/4,1/4,1/3],
    [1,1/2,1]
])

# Defining the security parameters of the network
securityParameters = [1/6,1/2,1/3]

# Defining the trust function between nodes and networks
def individualTrust(network, forward=True):
    
    # Initializing the network and empty trust values
    networkSize = len(network)
    trustSum = np.zeros(networkSize)
    
    # Computing the trust sum for all nodes i for r_i(N)
    if forward == True:
        for i in range(networkSize):
            trustSum[i] =  1/(networkSize) * np.sum(network[i])
             
    # Computing the trust sum for all nodes i for r_N(i)
    if forward == False:
        for i in range(networkSize):
            trustSum[i] =  1/(networkSize) * np.sum(network.T[i])
    
    return trustSum

# Defining the boolean decision function between nodes and networks
def booleanDecision(network, securityParameters):
    
    # Computing the size and individual trusts among the network
    networkSize = len(network)
    innerTrust = individualTrust(network)
    
    # Initializing empty array of boolean values
    booleanArray = np.zeros(networkSize)
    
    # Looping through and updating boolean array based on parameters
    for i in range(networkSize):
        if innerTrust[i] <= securityParameters[i]:
            booleanArray[i] = 1
            
    return booleanArray

# Defining the trust function between networks   
def networkTrust(firstNetwork, secondNetwork, forward=True):
    
    # Computing the individual trusts amongst the networks
    firstNetworkTrusts = individualTrust(firstNetwork)
    secondNetworkTrusts = individualTrust(secondNetwork)
    
    # Computing the trust between networks for r(N,N')
    if forward == True:
        totalNetworkTrust = np.max(firstNetworkTrusts)
    
    # Computing the trust between networks for r(N',N)
    if forward == False:
        totalNetworkTrust = np.max(secondNetworkTrusts)
        
    return totalNetworkTrust
    
# Testing the function on different networks
print('--- Trust of nodes amongst same network ---')
print(
    individualTrust(initialNetwork)
    )
print(
    individualTrust(initialNetwork,False)
    )
print('--- Security parameters ---')
print(securityParameters)
print('--- Boolean decision outcome ---')
print(
    booleanDecision(initialNetwork,securityParameters)
    )
print('--- Trust between different networks ---')
print(
    networkTrust(perspectiveNetwork,reversedNetwork)
    )
print(
    networkTrust(perspectiveNetwork,reversedNetwork,False)
    )


# %%
