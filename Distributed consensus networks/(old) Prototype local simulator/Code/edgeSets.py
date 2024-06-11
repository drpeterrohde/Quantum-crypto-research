#%% Importing modules - コンプリート

# Standard mathematics modules
import numpy as np
import matplotlib.pyplot as plt

# Group theoretic modules
from sympy.utilities.iterables import multiset_permutations


#%% Defining test edge sets to permute - コンプリート
testEdgeSet = [
        [1,2],[2,1],[2,3],[3,2],[4,4]
    ]

largeEdgeSet = [
        [1,1],[1,2],[2,1],[3,2],[3,3],[4,1],[5,2]
    ]

trivialEdgeSet = [
        [1,1],[2,2],[3,3]
        ]


# %% Redefining the consensus shuffle using the DCN notation - コンプリート

# Defining the consensus shuffle with a deterministic run time
def consensusShuffle(targetEdgeSet, extraInfo=True):
    
    # Initializing the edge set and its columns
    edgeSet = targetEdgeSet.copy()
    u = list(np.array(edgeSet).T[0])
    v = list(np.array(edgeSet).T[1])
    
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
        t = [i]
        
        # Constructing the transition set based on non-degenerate elements
        for k in range(
            0, i
            ):
            
            # Extra info: print if tuples occur in the edge set
            if extraInfo == True:
                print('[u[i],v[k]] tuple: ', [u[i],v[k]], [u[i],v[k]] not in edgeSet)
                print('[u[k],v[i]] tuple: ', [u[k],v[i]], [u[k],v[i]] not in edgeSet)
            
            # Appending non-degenerate points indices to the transition set
            if (
                ([u[i],v[k]] not in edgeSet) and ([u[k],v[i]] not in edgeSet)
                ):
                t.append(k)
                
        # Extra info: printing the transition set
        if extraInfo == True:
            print('Current transition index set: ', sorted(t))        
                
        # Randomly selecting a point in the transition set and swapping elements
        j = np.random.choice(t)
        u[i], u[j] = u[j], u[i]
        
        # Extra info: printing randomly selected element
        if extraInfo == True:
            print('Selected transition index: ', j)
            print('Selected swap point in U: ', u[i])
        
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

# Testing the function on different edge sets
print('--- Trivial Edge Set ---')
consensusShuffle(trivialEdgeSet)
print('--- Test Edge Set ---')
consensusShuffle(testEdgeSet)
print('--- Large Edge Set ---')
consensusShuffle(largeEdgeSet)
                

# %% [Vertex Space] Computing probability distribution of group action for the consensus group - コンプリート

# Defining a plotting function for a fixed amount of iterations
def probabilityDistribution(inputEdgeSet, edgeName, iterationSize, extraInfo=False):
    
    # Defining all possible unique permutations of the input set
    permutationArray = list(
        multiset_permutations(list(np.array(inputEdgeSet).T[0]))
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
probabilityDistribution(trivialEdgeSet,'trivialEdgeSet', 10000)
print('--- Test Edge Set ---')
probabilityDistribution(testEdgeSet,'testEdgeSet', 10000)
print('--- Large Edge Set ---')
probabilityDistribution(largeEdgeSet,'largeEdgeSet', 10000)


# %% Testing grounds for vertex space transformations
startingEdgeSet = [
    [1,1],[2,2]
    ]
print('Test edge set: ', testEdgeSet)
print('Starting edge set: ', startingEdgeSet)

# Different columns
uColumn = list(
    np.array(startingEdgeSet).T[0]
    )
vColumn = list(
    np.array(startingEdgeSet).T[1]
    )
reconstructedSet = np.column_stack(
    (uColumn,vColumn)
).tolist()
  
print('U Column: ', uColumn)
print('V Column: ', vColumn)

# Possible edge sets to compare to
possibleUColumns = list(
        multiset_permutations(uColumn)
    )
possibleVColumns = list(
        multiset_permutations(vColumn)
    )
print('Reconstructed edge set: ', reconstructedSet)
print('Possible U Columns: ', possibleUColumns)
print('Possible V Columns: ', possibleVColumns)
degeneratePossibleEdgeSets = [
    np.column_stack((u,v)).tolist() for u in possibleUColumns for v in possibleVColumns
]
print('Possible edge sets: ', degeneratePossibleEdgeSets)

# Cutting out degenerate entries in the possible edge sets
def removeDegeneracy(inputEdgeSets): 
    
    # Initializing the new list of unique edge sets
    uniqueEdgeSets = []

    # Initialize an empty set to keep track of duplicate edge sets
    seenEdgeSets = set()

    # Iterate through each inner edge set
    for edgeSet in inputEdgeSets:
        
        # Convert the inner list to a frozenset for immutability
        frozenSet = frozenset(map(tuple, edgeSet))

        # Check if the set is not in seen_sets (i.e., not a duplicate)
        if frozenSet not in seenEdgeSets:
            
            # Add the set to seenEdgeSets to mark it as seen
            seenEdgeSets.add(frozenSet)

            # Append the original inner list to unique_lsts
            uniqueEdgeSets.append(edgeSet)

    # Return the list of unique lists
    return uniqueEdgeSets

possibleEdgeSets = removeDegeneracy(degeneratePossibleEdgeSets)
print('Unique possible edge sets: ', possibleEdgeSets)


# %% [Edge Space] Computing probability distribution of group action for the consensus group - コンプリート

# Defining a plotting function for a fixed amount of iterations
def probabilityDistribution(inputEdgeSet, edgeName, iterationSize, extraInfo=False):
    
    # Defining the different columns of the edgeset
    uColumn = list(
        np.array(inputEdgeSet).T[0]
    )
    vColumn = list(
        np.array(inputEdgeSet).T[1]
    )

    # Defining all possible unique permutations of the edge set
    possibleUColumns = list(
        multiset_permutations(uColumn)
    )
    possibleVColumns = list(
        multiset_permutations(vColumn)
    )
    degeneratePossibleEdgeSets = [
        np.column_stack((u,v)).tolist() for u in possibleUColumns for v in possibleVColumns
    ]
    possibleEdgeSets = removeDegeneracy(degeneratePossibleEdgeSets)
    print('Total edge sets: ', len(possibleEdgeSets))
    print('All possible unique edge sets: ', possibleEdgeSets)

    # Initialize an empty list to tally up the occurences of given permutations
    tallySet = list(
        np.zeros(
            len(possibleEdgeSets), dtype=int
        )
    )
    
    # Iterating through iterationSize independent shuffles
    for iteration in range(
        1,iterationSize+1
        ):
        
        # Performing a random permutation of the U column of the edge set
        outputEdgeSet = consensusShuffle(inputEdgeSet,False).tolist()
        
        # Checking if it is one of the permutations and if so add to the tally
        for permutation in range(
            0,len(possibleEdgeSets)
        ):
            if outputEdgeSet in possibleEdgeSets:
                tallySet[permutation] += 1
            
    # Extra info: printing output tally set
    if extraInfo == True:           
        print('Final tally: ',tallySet)

    # Indexing all unique permutations of the edge set
    permutationIndexSet = list(
        np.arange(
            1, len(possibleEdgeSets)+1
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
    ax.axhline(y=1/len(possibleEdgeSets), color='gray', label = 'Expected Average Probability', linestyle = 'dotted')
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
    ax.grid()
    ax.set_axisbelow(True)
    
    return possibleEdgeSets


# Computing the probability distributions for the different edge sets
print('--- Starting Edge Set ---')
probabilityDistribution(startingEdgeSet,'startingEdgeSet',10000)
print('--- Trivial Edge Set ---')
probabilityDistribution(trivialEdgeSet,'trivialEdgeSet',10000)
print('--- Test Edge Set ---')
probabilityDistribution(testEdgeSet,'testEdgeSet',10000)


# %% Constructing a function to verify if a given degree sequence is satisfiable - コンプリート

# Defining the verification function for degree sequences
def sequenceVerifier(inputSequence, uSize, vSize, extraInfo=True):
    
    # Partioning degree sequence into ordered sub-sequences
    uSequence = sorted(
        inputSequence[:uSize], reverse=True
    )
    vSequence = sorted(
        inputSequence[vSize:], reverse=True
    )
    
    # Extra info: printing initial state of sequences
    if extraInfo == True:
        print('Partial U sequence: ', uSequence)
        print('Partial V sequence: ', vSequence)
    
    # Initializing constraint logic
    firstConstraint = False
    secondConstraint = False
    totalConstraint = False
    
    # Testing the first constraint: conservation
    if np.sum(uSequence) == np.sum(vSequence):
        firstConstraint = True
        
        # Extra info: printing the outcome of the first constraint
        if extraInfo == True:
            print('First constraint: ', firstConstraint)
        
    else:
        
        # Extra info: printing the outcome of the first constraint
        if extraInfo == True:
            print('First constraint: ', firstConstraint)
            
        return False
    
    # Testing the second constraint: boundedness
    for k in range(0, uSize):
        
        # Computing LHS of constraint
        leftHandSide = np.sum(uSequence[:k+1])
        
        # Computing RHS of constraint
        minVSequence = [min(v,k+1) for v in vSequence]
        rightHandSide = np.sum(minVSequence)
        
        # Extra info: printing the values of the sides
        if extraInfo == True:
            print('LHS: ', leftHandSide)
            print('RHS: ', rightHandSide)
        
        # Break loop if it doesn't satistfy each constraint for k
        if not leftHandSide <= rightHandSide:
            
            # Extra info: printing the outcome of the first constraint
            if extraInfo == True:
                print('Second constraint: ', secondConstraint)
                
            return False
    
    # If loop didn't break, then the second constraint is satisfied
    secondConstraint = True
    
    # Extra info: printing the outcome of the first constraint
    if extraInfo == True:
        print('Second constraint: ', secondConstraint)
    
    # If both constraints are sastisfied, it is a proper degree sequence
    if (firstConstraint == True) and (secondConstraint == True):
        totalConstraint = True
        
    # Returning output of the constraint
    return totalConstraint
    
# Printing some examples of the algorithm on degree sequences
print('--- Trivial degree sequence ---')
sequenceVerifier([1,1,1,1,1,1],3,3)
print('--- Non-trivial degree sequence ---')
sequenceVerifier([2,2,2,2,3,1],3,3)
print('--- Non-satisfying degree sequence ---')
sequenceVerifier([6,2,1,3,3,3],3,3)


# %% Constructing a function to output an intial graph assignment - コンプリート

# Defining the function from which outputs an edge assignment from U,V
def edgeAssignment(inputSequence, uSize, vSize, extraInfo=True):
    
    # Testing if is a satisfiable degree sequence
    if sequenceVerifier(inputSequence, uSize, vSize, False) == False:
        return False
    else:
        print('Partially satisfiable sequence.')
    
    # Initializing the ordered degree sequences and edge set
    edgeSet = []
    uSequence = sorted(
        inputSequence[:uSize], reverse=True
    )
    vSequence = sorted(
        inputSequence[vSize:], reverse=True
    )
    
    # Extra info: printing initial state of sequences and edge set
    if extraInfo == True:
        print('Partial U sequence: ', uSequence)
        print('Partial V sequence: ', vSequence)
        print('Initial edge set: ', edgeSet)
    
    # Looping through to construct the edge set
    for u in range(0,len(uSequence)):
        for v in range(0,len(vSequence)):
            if (uSequence[u]>0) and (vSequence[v]>0):
                edgeSet.append([u,v])
                uSequence[u] -= 1
                vSequence[v] -= 1
                
    # Extra info: printing the final state of the edge set
    if extraInfo == True:
        print('Final edge set: ', edgeSet)
              
    # Recall: the final graph has its columns decreasingly ordered!  
    return edgeSet
    
# Printing some examples of the algorithm on degree sequences
print('--- Trivial degree sequence ---')
edgeAssignment([1,1,1,1,1,1],3,3)
print('--- Non-trivial degree sequence ---')
edgeAssignment([2,2,2,2,3,1],3,3)
print('--- Non-satisfying degree sequence ---')
edgeAssignment([6,2,1,3,3,3],3,3)


# %%

