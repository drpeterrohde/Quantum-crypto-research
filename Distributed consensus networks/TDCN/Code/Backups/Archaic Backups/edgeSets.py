#%% Importing modules - コンプリート

# Standard mathematics modules
import numpy as np
import matplotlib.pyplot as plt

# Group theoretic modules
from sympy.utilities.iterables import multiset_permutations


#%% Defining test edge sets to permute - コンプリート
testEdgeSet = np.array(
    [
        [1,2],[2,1],[2,3],[3,2],[4,4]
    ]
)
largeEdgeSet = np.array(
    [
        [1,1],[1,2],[2,1],[3,2],[3,3],[4,1],[5,2]
    ]
)
trivialEdgeSet = np.array(
    [
        [1,1],[2,2],[3,3]
    ]
)


# %% Redefing the consensus shuffle using the DCN notation - コンプリート

# Defining the consensus shuffle with a deterministic run time
def consensusShuffle(targetEdgeSet, extraInfo=True):
    
    # Initializing the edge set and its columns
    edgeSet = np.copy(targetEdgeSet)
    u = list(edgeSet.T[0]) #\vec{u}
    v = list(edgeSet.T[1]) #\vec{v}
    
    # Extra info: printing the original configuration of the set
    if extraInfo == True:
        print('Initial edge set of the graph:\n', edgeSet)
        print('Target list:\n', u)
        print('Dual list:\n', v)
        
    # Looping over the different endpoints of the unselected elements
    for i in reversed(
        range(
            1, len(u)
        )
    ):
        # Extra info: printing current selected endpoint
        if extraInfo == True:
            print('Current endpoint: ', u[i])
        
        # Initializing the transition index set
        t = []
        
        # Constructing the transition set based on non-degenerate elements
        for k in range(
            0, i+1
            ):
            
            # Appending non-degenerate points to the transition set
            if (
                ((u[i] != u[k]) and (v[i] != v[k])) or ((u[i] == u[k]) and (v[i] == v[k]))
                ):
                t.append(k)
                
        # Extra info: printing the transition set
        if extraInfo == True:
            print('Current transition index set: ', t)        
                
        # Randomly selecting a point in the transition set and swapping elements
        j = np.random.choice(t)
        u[i], u[j] = u[j], u[i]
        
        # Extra info: printing randomly selected element
        if extraInfo == True:
            print('Selected transition point: ', j)
            print('Selected point in U: ', u[i])
        
        # Extra info: printing swapped elements and new list
        if extraInfo == True:
            print('Swapped element', u[i], 'with', u[j])
            print('Current target list: ', u)
            print('Current dual list: ', v)
        
    # Gluing back the pieces of the edge set together 
    finalEdgeSet = np.column_stack(
        (u,v)
    )
    
    # Extra info: presenting the final state of the edge set
    if extraInfo == True:
        print('Final state of edge set:\n', finalEdgeSet)
        
    return finalEdgeSet
                

# %% Testing out on different edge sets - コンプリート

# Testing the function on the trivial edge set
print('--- Trivial Edge Set ---')
consensusShuffle(trivialEdgeSet)

# Testing the function on the test edge set
print('--- Test Edge Set ---')
consensusShuffle(testEdgeSet)

# Testing the function on the test edge set
print('--- Large Edge Set ---')
consensusShuffle(largeEdgeSet)


# %% [Vertex Space] Computing probability distribution of group action for the consensus group - コンプリート

# Defining a plotting function for a fixed amount of iterations
def probabilityDistribution(inputEdgeSet, edgeName, iterationSize, extraInfo=False):
    
    # Defining all possible unique permutations of the input set
    permutationArray = list(
        multiset_permutations(list(inputEdgeSet.T[0]))
    )
    print('Total possible permutations: ', len(permutationArray))
    print('All possible unique permutations: ', permutationArray)

    # Initialize an empty list to tally up the occurences of given permutations
    tallySet = list(
        np.zeros(
            len(permutationArray), dtype=int
        )
    )
    
    # Iterating through iterationSize independent shuffles
    for iteration in range(
        1,iterationSize+1
        ):
        
        # Performing a random permutation of the U column of the edge set
        outputEdgeSet = consensusShuffle(inputEdgeSet,False)
        outputTargetList = list(outputEdgeSet.T[0])
        if extraInfo == True:
            print('Permuted set: ', outputTargetList)
        
        # Checking if it is one of the permutations and if so add to the tally
        for permutation in range(
            0,len(permutationArray)
        ):
            if outputTargetList == permutationArray[permutation]:
                tallySet[permutation] += 1
            
    # Extra info: printing output tally set
    if extraInfo == True:           
        print('Final tally: ',tallySet)

    # Indexing all unique permutations of U
    permutationIndexSet = list(
        np.arange(
            1, len(permutationArray)+1
        )
    )
    
    # Computing the average occurence of the unique permutations
    averageOccurence = np.mean(tallySet)/iterationSize
    
    # Probability set of all unique permutations of U
    probabilitySet = np.array(tallySet)/iterationSize

    # Plotting results of permutations for all independent iterations
    fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)
    
    # Top subplot: probabilities
    ax = axs[0]
    ax.scatter(permutationIndexSet,probabilitySet, color='magenta',label='Probabilities')
    ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average Probability')
    ax.axhline(y=1/len(permutationArray), color='gray', label = 'Expected Average Probability', linestyle = 'dotted')
    ax.set_ylabel('Permutation Probability')
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax.set_title(f'{iterationSize} Independent Shuffles for {edgeName}')
    ax.legend()
    ax.grid()
    ax.set_axisbelow(True)

    # Bottom subplot: residuals
    ax = axs[1]
    ax.scatter(permutationIndexSet,np.abs(
        ( np.array(tallySet)/iterationSize ) - averageOccurence
    ), color ='aqua', label='Normalized Residues')
    ax.set_xlabel('Unique Permutations')
    ax.set_ylabel('Logarithmic Variance')
    ax.set_yscale('log')
    ax.grid()
    ax.set_axisbelow(True)
    
    return

# Computing the probability distributions for the different edge sets
print('--- Trivial Edge Set ---')
probabilityDistribution(trivialEdgeSet,'trivialEdgeSet',10000)
print('--- Test Edge Set ---')
probabilityDistribution(testEdgeSet,'testEdgeSet',10000)
print('--- Large Edge Set ---')
probabilityDistribution(largeEdgeSet,'largeEdgeSet',10000)


# %% [Edge Space] Computing probability distribution of group action for the consensus group - コンプリート

# Defining a plotting function for a fixed amount of iterations
def probabilityDistribution(inputEdgeSet, edgeName, iterationSize, extraInfo=False):
    
    # Defining all possible unique permutations of the input set
    permutationArray = list(
        multiset_permutations(list(inputEdgeSet.T[0]))
    )
    print('Total possible permutations: ', len(permutationArray))
    print('All possible unique permutations: ', permutationArray)

    # Initialize an empty list to tally up the occurences of given permutations
    tallySet = list(
        np.zeros(
            len(permutationArray), dtype=int
        )
    )
    
    # Iterating through iterationSize independent shuffles
    for iteration in range(
        1,iterationSize+1
        ):
        
        # Performing a random permutation of the U column of the edge set
        outputEdgeSet = consensusShuffle(inputEdgeSet,False)
        outputTargetList = list(outputEdgeSet.T[0])
        if extraInfo == True:
            print('Permuted set: ', outputTargetList)
        
        # Checking if it is one of the permutations and if so add to the tally
        for permutation in range(
            0,len(permutationArray)
        ):
            if outputTargetList == permutationArray[permutation]:
                tallySet[permutation] += 1
            
    # Extra info: printing output tally set
    if extraInfo == True:           
        print('Final tally: ',tallySet)

    # Indexing all unique permutations of U
    permutationIndexSet = list(
        np.arange(
            1, len(permutationArray)+1
        )
    )
    
    # Computing the average occurence of the unique permutations
    averageOccurence = np.mean(tallySet)/iterationSize
    
    # Probability set of all unique permutations of U
    probabilitySet = np.array(tallySet)/iterationSize

    # Plotting results of permutations for all independent iterations
    fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)
    
    # Top subplot: probabilities
    ax = axs[0]
    ax.scatter(permutationIndexSet,probabilitySet, color='magenta',label='Probabilities')
    ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average Probability')
    ax.axhline(y=1/len(permutationArray), color='gray', label = 'Expected Average Probability', linestyle = 'dotted')
    ax.set_ylabel('Permutation Probability')
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax.set_title(f'{iterationSize} Independent Shuffles for {edgeName}')
    ax.legend()
    ax.grid()
    ax.set_axisbelow(True)

    # Bottom subplot: residuals
    ax = axs[1]
    ax.scatter(permutationIndexSet,np.abs(
        ( np.array(tallySet)/iterationSize ) - averageOccurence
    ), color ='aqua', label='Normalized Residues')
    ax.set_xlabel('Unique Permutations')
    ax.set_ylabel('Logarithmic Variance')
    ax.set_yscale('log')
    ax.grid()
    ax.set_axisbelow(True)
    
    return

# Computing the probability distributions for the different edge sets
print('--- Trivial Edge Set ---')
probabilityDistribution(trivialEdgeSet,'trivialEdgeSet',10000)
print('--- Test Edge Set ---')
probabilityDistribution(testEdgeSet,'testEdgeSet',10000)
print('--- Large Edge Set ---')
probabilityDistribution(largeEdgeSet,'largeEdgeSet',10000)


# %% Initialize a satisfying edge set from a given degree sequence  - コンプリート

# This is following Peters comments on signal + algorithmn 8

