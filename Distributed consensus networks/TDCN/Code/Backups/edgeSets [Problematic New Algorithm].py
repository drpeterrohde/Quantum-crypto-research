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



# %% Redefing the consensus shuffle using the DCN notation - コンプリート

# Defining the consensus shuffle with a deterministic run time
def consensusShuffle(targetEdgeSet, extraInfo=True):
    
    # Initializing the edge set and its columns
    edgeSet = targetEdgeSet.copy()
    u = list(np.array(edgeSet).T[0]) #\vec{u}
    v = list(np.array(edgeSet).T[1]) #\vec{v}
    
    
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
            0, i #REMOVED +1
            ):
            
            print('[u[i],v[k]] tuple: ', [u[i],v[k]])
            print('[u[k],v[i]]tuple: ', [u[k],v[i]])
            
            print('not in edges: ',([u[i],v[k]] not in edgeSet))
            
            # Appending non-degenerate points to the transition set
            if (
                ([u[i],v[k]] not in edgeSet) and ([u[k],v[i]] not in edgeSet)
                ):
                print('satisfied')
                t.append(k)
            print('string k',k)
        
        # Adding current index i to the transition set
        # t.append(i)
        # t = sorted(t)
                
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


# %% Constructing an initial degree sequence - コンプリート

# Initializing disordered degree sets for the vertices U,V
uDegree = [1,7,4,2]
vDegree = [3,5,2,1]

# Sorting the different degree sets into partial degree sequences
uSequence = sorted(uDegree, reverse=True)
vSequence = sorted(vDegree, reverse=True)
print('Ordered U degree sequence: ', uSequence)
print('Ordered V degree sequence: ', vSequence)


# Combining into the full degree sequence
degreeSequence = uSequence + vSequence
print('Full degree sequence: ', degreeSequence)

# Given a degree sequence we can recover partial sequences via |U|
partialUSequence = degreeSequence[:len(uDegree)]
partialVSequence = degreeSequence[len(vDegree):]
print(uSequence == partialUSequence)
print(vSequence == partialVSequence)


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
    for k in range(1, uSize+1):
        
        # Computing LHS of constraint
        leftHandSide = np.sum(uSequence[:k+1])
        
        # Computing RHS of constraint
        minVSequence = [min(v,k) for v in vSequence]
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
    
# Printing some examples of the algorithm
print('--- Example non-satisfying sequence ---')
sequenceVerifier([1,2,3,4,1,2,3,4],4,4)
print('--- Example satisfying sequence ---')
sequenceVerifier([1,1,2,1,1,2],3,3)


# %% Constructing a function to output an intial graph assignment - コンプリート

# Defining the function from which outputs an edge assignment from U,V
def edgeAssignment(inputSequence, uSize, vSize, extraInfo=True):
    
    # Testing if is a satisfiable degree sequence
    if sequenceVerifier(inputSequence, uSize, vSize, False) == False:
        return False
    else:
        print('Satisfiable sequence.')

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
    for u in uSequence:
        for v in vSequence:
            if (u>0) and (v>0):
                edgeSet.append([u,v])
    
    print('Final edge set: ', edgeSet)
    
    
# %%
edgeAssignment([1,1,2,1,1,2],3,3)


# %%
