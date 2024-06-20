#%% Importing modules - コンプリート

# Standard mathematics modules
import numpy as np
import matplotlib.pyplot as plt
import random

# Group theoretic modules
from sympy.utilities.iterables import multiset_permutations
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import (SymmetricGroup, CyclicGroup, DihedralGroup)
# Notes: random


#%% Defining modern & general Fisher Yates shuffles for different symmetry groups - コンプリート

# Defining the modern Fisher Yates swapping function
def FisherYates(inputSet,extraInfo=True):
    
    # Making a copy of the input to no overwrite it
    inputArray = inputSet.copy()
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            1, len(inputArray)
        )
    ):
        # Select a random array element (bounded by included endpoints)
        randomIndex = np.random.randint(0, endpoint+1)
        randomElement = inputArray[randomIndex]
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', inputArray[endpoint], end='.\n')
        inputArray[randomIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    return inputArray


# Defining the generalized Fisher Yates swapping function (G = permutation)
def permutationFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    initializedSet = Permutation(inputArray)
    permutationGroup = PermutationGroup([initializedSet])
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            1, len(inputArray)
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            permutationGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Defining the intersection of the orbit and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & set(lastElementOrbit)
        )
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    return inputArray


# Defining the generalized Fisher Yates swapping function (G = symmetric)
def symmetricFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    symmetricGroup = SymmetricGroup(
        len(inputArray)
    )
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            1, len(inputArray)
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            symmetricGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Defining the intersection of the orbit and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & set(lastElementOrbit)
        )
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    return inputArray


# Defining the generalized Fisher Yates swapping function (G = cyclic)
def cyclicFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    cyclicGroup = CyclicGroup(
        len(inputArray)
    )
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            1, len(inputArray)
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            cyclicGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Defining the intersection of the orbit and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & set(lastElementOrbit)
        )
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    return inputArray


# Defining the generalized Fisher Yates swapping function (G = dihedral)
def dihedralFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    dihedralGroup = DihedralGroup(
        len(inputArray)
    )
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            1, len(inputArray)
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            dihedralGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Defining the intersection of the orbit and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & set(lastElementOrbit)
        )
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    return inputArray


#%% Performing different group actions on sample input sets - コンプリート

# Selecting a random permutation of {0,...,n} as out input array
inputState = [0,1,2,3,4]
possiblePermutations = possiblePermutations = list(
    multiset_permutations(inputState)
)
selectedPermutation = possiblePermutations[
    np.random.randint(0,len(possiblePermutations))
]
print('Selected permutation for different groups: ', selectedPermutation)


# Peforming different transformations for different groups
print('--- Modern Fisher Yates ---')
FisherYates(selectedPermutation)
print('--- Generalized Fisher Yates (Permutation Group) ---')
permutationFisherYates(selectedPermutation)
print('--- Generalized Fisher Yates (Symmetric Group) ---')
symmetricFisherYates(selectedPermutation)
print('--- Generalized Fisher Yates (Cyclic Group) ---')
cyclicFisherYates(selectedPermutation)
print('--- Generalized Fisher Yates (Dihedral Group) ---')
dihedralFisherYates(selectedPermutation)


# %% Computing probability distribution of group action for different Fisher Yates shuffles - コンプリート

# Defining a plotting function for a fixed amount of iterations
def groupDistribution(shuffleAlgorithm, inputSet, iterationSize, extraInfo=False):
    
     #Defining all possible unique permutations of the input set
    permutationArray = list(
        multiset_permutations(inputSet)
    )

    # Initialize an empty list to tally up the occurences of given permutations
    tallySet = list(
        np.zeros(
            len(permutationArray), dtype=int
        )
    )
    
    # Iterating through iterations of shuffles
    for iteration in range(1,iterationSize+1):
        
        # Performing a random permutation of the input set
        outputSet = shuffleAlgorithm(inputSet,False)
        if extraInfo == True:
            print('Permuted set: ',outputSet)
        
        # Checking if it is one of the permutations and if so add to the tally
        for permutation in range(
            len(permutationArray)
        ):
            if outputSet == permutationArray[permutation]:
                tallySet[permutation] += 1
            
    # Printing output tally set
    if extraInfo == True:           
        print('Final tally: ',tallySet)

    # Plotting results
    permutationIndexSet = list(
        np.arange(
            1, len(permutationArray)+1
        )
    )
    averageOccurence = np.mean(tallySet)/iterationSize

    fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)

    ax = axs[0]
    ax.scatter(permutationIndexSet,np.array(tallySet)/iterationSize, color='magenta',label='Frequency')
    ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average Probability')
    ax.axhline(y=1/len(permutationArray), color='gray', label = 'Expected Average Probability', linestyle = 'dotted')
    ax.set_ylabel('Permutation Probability')
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax.set_title(f'{iterationSize} Independent Shuffles with {shuffleAlgorithm.__name__}')
    ax.legend()
    ax.grid()
    ax.set_axisbelow(True)

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


# Computing probability distribution for different group actions
print('--- Modern Fisher Yates ---')
groupDistribution(FisherYates,selectedPermutation,100000)
print('--- Generalized Fisher Yates (Permutation Group) ---')
groupDistribution(permutationFisherYates,selectedPermutation,100000)
print('--- Generalized Fisher Yates (Symmetric Group) ---')
groupDistribution(symmetricFisherYates,selectedPermutation,100000)
print('--- Generalized Fisher Yates (Cyclic Group) ---')
groupDistribution(cyclicFisherYates,selectedPermutation,100000)
print('--- Generalized Fisher Yates (Dihedral Group) ---')
groupDistribution(dihedralFisherYates,selectedPermutation,100000)


#%% Defining general Fisher Yates shuffles with orbit probabilities - コンプリート

# Defining the generalized orbit Fisher Yates swapping function (G = permutation)
def permutationOrbitFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    initializedSet = Permutation(inputArray)
    permutationGroup = PermutationGroup([initializedSet])
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
        
    # Initializing inverse orbit size list
    inverseOrbitSizes = list(
        np.zeros(
            len(inputArray)
        )
    )
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            0, len(inputArray) #CHANGED TO 0 INSTEAD OF 1
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            permutationGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Defining the intersection of the orbit and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & set(lastElementOrbit)
        )
        overlapSize = len(overlapList)
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
            print('Transition set size: ', overlapSize)
        inverseOrbitSizes[endpoint] = 1/overlapSize
        if extraInfo == True:
            print('Inverse Transition Size: ', 1/overlapSize)
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    # Multiplying all elements of inverseOrbitSizes for final permutation probality
    permutationProbability = np.prod(inverseOrbitSizes)
    if extraInfo == True:     
        print('Final inverse orbit sizes: ', inverseOrbitSizes)
        print('Final permutation probability: ', permutationProbability)
        
    return inputArray, permutationProbability


# Defining the generalized orbit Fisher Yates swapping function (G = symmetric)
def symmetricOrbitFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    symmetricGroup = SymmetricGroup(
        len(inputArray)
    )
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
        
    # Initializing inverse orbit size list
    inverseOrbitSizes = list(
        np.zeros(
            len(inputArray)
        )
    )
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            0, len(inputArray) #CHANGED TO 0 INSTEAD OF 1
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            symmetricGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Defining the intersection of the orbit and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & set(lastElementOrbit)
        )
        overlapSize = len(overlapList)
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
            print('Transition set size: ', overlapSize)
        inverseOrbitSizes[endpoint] = 1/overlapSize
        if extraInfo == True:
            print('Inverse Transition Size: ', 1/overlapSize)
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    # Multiplying all elements of inverseOrbitSizes for final permutation probality
    permutationProbability = np.prod(inverseOrbitSizes)
    if extraInfo == True:     
        print('Final inverse orbit sizes: ', inverseOrbitSizes)
        print('Final permutation probability: ', permutationProbability)
        
    return inputArray, permutationProbability


# Defining the generalized orbit Fisher Yates swapping function (G = cyclic)
def cyclicOrbitFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    cyclicGroup = CyclicGroup(
        len(inputArray)
    )
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
        
    # Initializing inverse orbit size list
    inverseOrbitSizes = list(
        np.zeros(
            len(inputArray)
        )
    )
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            0, len(inputArray) #CHANGED TO 0 INSTEAD OF 1
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            cyclicGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Defining the intersection of the orbit and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & set(lastElementOrbit)
        )
        overlapSize = len(overlapList)
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
            print('Transition set size: ', overlapSize)
        inverseOrbitSizes[endpoint] = 1/overlapSize
        if extraInfo == True:
            print('Inverse Transition Size: ', 1/overlapSize)
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    # Multiplying all elements of inverseOrbitSizes for final permutation probality
    permutationProbability = np.prod(inverseOrbitSizes)
    if extraInfo == True:     
        print('Final inverse orbit sizes: ', inverseOrbitSizes)
        print('Final permutation probability: ', permutationProbability)
        
    return inputArray, permutationProbability


# Defining the generalized orbit Fisher Yates swapping function (G = dihedral)
def dihedralOrbitFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    dihedralGroup = DihedralGroup(
        len(inputArray)
    )
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
        
    # Initializing inverse orbit size list
    inverseOrbitSizes = list(
        np.zeros(
            len(inputArray)
        )
    )
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            0, len(inputArray) #CHANGED TO 0 INSTEAD OF 1
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            dihedralGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Defining the intersection of the orbit and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & set(lastElementOrbit)
        )
        overlapSize = len(overlapList)
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
            print('Transition set size: ', overlapSize)
        inverseOrbitSizes[endpoint] = 1/overlapSize
        if extraInfo == True:
            print('Inverse Transition Size: ', 1/overlapSize)
            
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    # Multiplying all elements of inverseOrbitSizes for final permutation probality
    permutationProbability = np.prod(inverseOrbitSizes)
    if extraInfo == True:     
        print('Final inverse orbit sizes: ', inverseOrbitSizes)
        print('Final permutation probability: ', permutationProbability)
        
    return inputArray, permutationProbability


#%% Performing different group actions on sample input sets - コンプリート

# Selecting a random permutation of {0,...,n} as out input array
inputState = [0,1,2,3,4]
possiblePermutations = possiblePermutations = list(
    multiset_permutations(inputState)
)
selectedPermutation = possiblePermutations[
    np.random.randint(0,len(possiblePermutations))
]
print('Selected permutation for different groups: ', selectedPermutation)


# Peforming different transformations for different groups
print('--- Generalized Fisher Yates (Permutation Group) ---')
permutationOrbitFisherYates(selectedPermutation)
print('--- Generalized Fisher Yates (Symmetric Group) ---')
symmetricOrbitFisherYates(selectedPermutation)
print('--- Generalized Fisher Yates (Cyclic Group) ---')
cyclicOrbitFisherYates(selectedPermutation)
print('--- Generalized Fisher Yates (Dihedral Group) ---')
dihedralOrbitFisherYates(selectedPermutation)


# %% Computing probability distribution of group action with orbit probabilities - コンプリート

# Defining a plotting function for a fixed amount of iterations
def groupOrbitDistribution(shuffleAlgorithm, inputSet, iterationSize, extraInfo=False):
    
     #Defining all possible unique permutations of the input set
    permutationArray = list(
        multiset_permutations(inputSet)
    )

    # Initialize an empty list to tally up the occurences of given permutations
    tallySet = list(
        np.zeros(
            len(permutationArray), dtype=int
        )
    )
    
    # Initialize an empty list of permutation probabilities
    probabilitySet = list(
        np.zeros(
            len(permutationArray), dtype=int
        )
    )
    
    # Iterating through iterations of shuffles
    for iteration in range(1,iterationSize+1):
        
        # Performing a random permutation of the input set
        fisherOutput = shuffleAlgorithm(inputSet,False)
        outputSet = fisherOutput[0]
        if extraInfo == True:
            print('Permuted set: ',outputSet)
        
        # Checking if it is one of the permutations and if so add to the tally
        for permutation in range(
            len(permutationArray)
        ):
            if outputSet == permutationArray[permutation]:
                tallySet[permutation] += 1
                probabilitySet[permutation] += fisherOutput[1]
            
    # Printing output tally set
    if extraInfo == True:           
        print('Final tally: ',tallySet)
        
    # Computed the predicted occurences based on inverse probabilities
    for i in range(
            len(permutationArray)
        ):
            probabilitySet[i] = (probabilitySet[i]/(tallySet[i]+0.0000000000000001)) # Added small number to avoid zero division

    # Plotting results
    permutationIndexSet = list(
        np.arange(
            1, len(permutationArray)+1
        )
    )
    averageOccurence = np.mean(tallySet)/iterationSize

    fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)

    ax = axs[0]
    ax.scatter(permutationIndexSet,np.array(tallySet)/iterationSize, color='magenta',label='Frequency')
    ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average Probability')
    ax.scatter(permutationIndexSet,probabilitySet, color='gray', label = 'Expected Averages', linestyle = 'dotted')
    ax.set_ylabel('Permutation Probability')
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax.set_title(f'{iterationSize} Independent Shuffles with {shuffleAlgorithm.__name__}')
    ax.legend()
    ax.grid()
    ax.set_axisbelow(True)

    ax = axs[1]
    ax.scatter(permutationIndexSet,np.abs(
        ( np.array(tallySet)/iterationSize ) - averageOccurence
    ), color ='aqua', label='Normalized Residues')
    ax.set_xlabel('Unique Permutations')
    ax.set_ylabel('Logarithmic Variance')
    ax.set_yscale('log')
    ax.grid()
    ax.set_axisbelow(True)
    
    print('Amount of unique selected permutations: ', np.count_nonzero(tallySet))
    
    return


# Computing probability distribution for different group actions
print('--- Generalized Fisher Yates (Permutation Group) ---')
groupOrbitDistribution(permutationOrbitFisherYates,selectedPermutation,100000)
print('--- Generalized Fisher Yates (Symmetric Group) ---')
groupOrbitDistribution(symmetricOrbitFisherYates,selectedPermutation,100000)
print('--- Generalized Fisher Yates (Cyclic Group) ---')
groupOrbitDistribution(cyclicOrbitFisherYates,selectedPermutation,100000)
print('--- Generalized Fisher Yates (Dihedral Group) ---')
groupOrbitDistribution(dihedralOrbitFisherYates,selectedPermutation,100000)


#%% Defining general non-degenerate Fisher Yates shuffles with orbit probabilities - コンプリート

# Defining the generalized orbit Fisher Yates swapping function (G = permutation) (probability divergence)

# Defining the generalized orbit Fisher Yates swapping function (G = symmetric)
def symmetricNDFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    symmetricGroup = SymmetricGroup(
        len(inputArray)
    )
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
        
    # Initializing inverse orbit size list
    inverseOrbitSizes = list(
        np.zeros(
            len(inputArray)
        )
    )
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            1, len(inputArray) #CHANGED BACK TO 1
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            symmetricGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
            
        # Look at the orbit (from the stabilizer subgroup) of the last element of the list
        stabilizerSubGroup = symmetricGroup.stabilizer(lastElement)
        stabilizerOrbit = list(
            stabilizerSubGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Stabilizer orbit of last element: ', stabilizerOrbit)
        
        # Defining the intersection of the orbit (removing stabilizer orbit) and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & ( set(lastElementOrbit) - set(stabilizerOrbit) )
        )
        overlapSize = len(overlapList)
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
            print('Transition set size: ', overlapSize)
        inverseOrbitSizes[endpoint] = 1/overlapSize
        if extraInfo == True:
            print('Inverse Transition Size: ', 1/overlapSize)
            
        # Removing problematic first entry
        inverseOrbitSizes[0] = 1.0
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    # Multiplying all elements of inverseOrbitSizes for final permutation probality
    permutationProbability = np.prod(inverseOrbitSizes)
    if extraInfo == True:     
        print('Final inverse orbit sizes: ', inverseOrbitSizes)
        print('Final permutation probability: ', permutationProbability)
        
    return inputArray, permutationProbability


# Defining the generalized orbit Fisher Yates swapping function (G = cyclic)
def cyclicNDFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    cyclicGroup = CyclicGroup(
        len(inputArray)
    )
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
        
    # Initializing inverse orbit size list
    inverseOrbitSizes = list(
        np.zeros(
            len(inputArray)
        )
    )
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            1, len(inputArray) #CHANGED BACK TO 1
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            cyclicGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Look at the orbit (from the stabilizer subgroup) of the last element of the list
        stabilizerSubGroup = cyclicGroup.stabilizer(lastElement)
        stabilizerOrbit = list(
            stabilizerSubGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Stabilizer orbit of last element: ', stabilizerOrbit)
        
        # Defining the intersection of the orbit (removing stabilizer orbit) and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & ( set(lastElementOrbit) - set(stabilizerOrbit) )
        )
        overlapSize = len(overlapList)
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
            print('Transition set size: ', overlapSize)
        inverseOrbitSizes[endpoint] = 1/overlapSize
        if extraInfo == True:
            print('Inverse Transition Size: ', 1/overlapSize)
            
        # Removing problematic first entry
        inverseOrbitSizes[0] = 1.0
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    # Multiplying all elements of inverseOrbitSizes for final permutation probality
    permutationProbability = np.prod(inverseOrbitSizes)
    if extraInfo == True:     
        print('Final inverse orbit sizes: ', inverseOrbitSizes)
        print('Final permutation probability: ', permutationProbability)
        
    return inputArray, permutationProbability


# Defining the generalized orbit Fisher Yates swapping function (G = dihedral)
def dihedralNDFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
    inputArray = inputSet.copy()
    dihedralGroup = DihedralGroup(
        len(inputArray)
    )
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
        
    # Initializing inverse orbit size list
    inverseOrbitSizes = list(
        np.zeros(
            len(inputArray)
        )
    )
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            1, len(inputArray) #CHANGED BACK TO 1
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = list(
            dihedralGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
        
        # Look at the orbit (from the stabilizer subgroup) of the last element of the list
        stabilizerSubGroup = dihedralGroup.stabilizer(lastElement)
        stabilizerOrbit = list(
            stabilizerSubGroup.orbit(lastElement)
        )
        if extraInfo == True:
            print('Stabilizer orbit of last element: ', stabilizerOrbit)
        
        # Defining the intersection of the orbit (removing stabilizer orbit) and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & ( set(lastElementOrbit) - set(stabilizerOrbit) )
        )
        overlapSize = len(overlapList)
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
            print('Transition set size: ', overlapSize)
        inverseOrbitSizes[endpoint] = 1/overlapSize
        if extraInfo == True:
            print('Inverse Transition Size: ', 1/overlapSize)
            
        # Removing problematic first entry
        inverseOrbitSizes[0] = 1.0
            
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    # Multiplying all elements of inverseOrbitSizes for final permutation probality
    permutationProbability = np.prod(inverseOrbitSizes)
    if extraInfo == True:     
        print('Final inverse orbit sizes: ', inverseOrbitSizes)
        print('Final permutation probability: ', permutationProbability)
        
    return inputArray, permutationProbability


#%% Performing different non-degenerate group actions on sample input sets - コンプリート

# Selecting a random permutation of {0,...,n} as out input array
inputState = [0,1,2,3,4]
possiblePermutations = possiblePermutations = list(
    multiset_permutations(inputState)
)
selectedPermutation = possiblePermutations[
    np.random.randint(0,len(possiblePermutations))
]
print('Selected permutation for different groups: ', selectedPermutation)


# Peforming different transformations for different groups
print('--- Generalized ND Fisher Yates (Symmetric Group) ---')
symmetricNDFisherYates(selectedPermutation)
print('--- Generalized ND Fisher Yates (Cyclic Group) ---')
cyclicNDFisherYates(selectedPermutation)
print('--- Generalized ND Fisher Yates (Dihedral Group) ---')
dihedralNDFisherYates(selectedPermutation)


# %% Computing probability distribution of non-degenerate group action with orbit probabilities - コンプリート

# Computing probability distribution for different group actions
print('--- Generalized ND Fisher Yates (Symmetric Group) ---')
groupOrbitDistribution(symmetricNDFisherYates,selectedPermutation,100000)
print('--- Generalized ND Fisher Yates (Cyclic Group) ---')
groupOrbitDistribution(cyclicNDFisherYates,selectedPermutation,100000)
print('--- Generalized ND Fisher Yates (Dihedral Group) ---')
groupOrbitDistribution(dihedralNDFisherYates,selectedPermutation,100000)

# Note: For a network size n, the amount of selected permutations modulo degeneracy is (n-1)!. If degeneracy is kept, then it is instead n!.

#%% Manually defining the Fisher Yates shuffles with orbit probabilities under the consensus group (symmetric group modulo degeneracies) - コンプリート

# Defining the consensus group Fisher Yates swapping function
def consensusFisherYates(inputSet,extraInfo=True):
    
    # Initializing the set to prevent it being overwritten
    inputArray = inputSet.copy()
    
    # Printing the original state of the array
    if extraInfo == True:
        print('Initial array state: ', inputArray)
        
    # Initializing inverse orbit size list
    inverseOrbitSizes = list(
        np.zeros(
            len(inputArray)
        )
    )
    
    # Looping over the different included endpoints of the array
    for endpoint in reversed(
        range(
            1, len(inputArray) #CHANGED BACK TO 1
        )
    ):
        # Look at the orbit of the last element of the list
        lastElement = inputArray[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastElement)
        lastElementOrbit = sorted(inputArray[:endpoint+1])
        if extraInfo == True:
            print('Orbit of last element: ', lastElementOrbit)
            
        # Look at the orbit (from the stabilizer subgroup) of the last element of the list
        stabilizerOrbit = [lastElement]
        if extraInfo == True:
            print('Stabilizer orbit of last element: ', stabilizerOrbit)
        
        # Defining the intersection of the orbit (removing stabilizer orbit) and the unselected list entries
        overlapList = list(
            set(inputArray[:endpoint+1]) & ( set(lastElementOrbit) - set(stabilizerOrbit) )
        )
        overlapSize = len(overlapList)
        if extraInfo == True:
            print('Transition overlap set: ', overlapList)
            print('Transition set size: ', overlapSize)
        inverseOrbitSizes[endpoint] = 1/overlapSize
        if extraInfo == True:
            print('Inverse Transition Size: ', 1/overlapSize)
            
        # Removing problematic first entry
        inverseOrbitSizes[0] = 1.0
        
        # Selecting a random element of the intersection/transition set
        randomIndex = np.random.randint(
            0, len(overlapList)
            )
        randomElement = overlapList[randomIndex]
        randomElementInputIndex = inputArray.index(randomElement)
        if extraInfo == True:
            print('Array element', randomElement, 'of index', randomElementInputIndex, 'selected.')
            
        # Swapping the randomly selected element with the current array endpoint
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastElement, end='.\n')
        inputArray[randomElementInputIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomElementInputIndex]
        if extraInfo == True:
            print('New array state: ', inputArray)
            
    # Presenting the final state of the array
    if extraInfo == True:
        print('Final array state: ', inputArray)
        
    # Multiplying all elements of inverseOrbitSizes for final permutation probality
    permutationProbability = np.prod(inverseOrbitSizes)
    if extraInfo == True:     
        print('Final inverse orbit sizes: ', inverseOrbitSizes)
        print('Final permutation probability: ', permutationProbability)
        
    return inputArray, permutationProbability


# %% Computing probability distribution of non-degenerate group action with orbit probabilities - コンプリート

# Selecting a random permutation of {0,...,n} as out input array
inputState = [0,1,2,3,4]
possiblePermutations = possiblePermutations = list(
    multiset_permutations(inputState)
)
selectedPermutation = possiblePermutations[
    np.random.randint(0,len(possiblePermutations))
]
print('Selected permutation for different groups: ', selectedPermutation)

# Performing consensus shuffle on selected permutation
print('--- Consensus Fisher Yates (Consensus Group) ---')
consensusFisherYates(selectedPermutation)

# Computing probability distribution for the consensus group
print('--- Consensus Fisher Yates (Consensus Group) ---')
groupOrbitDistribution(consensusFisherYates,selectedPermutation,100000)


# %% Consctruction of the edge sets for proper permutation - コンプリート

# Defining the edge set
testEdgeSet = np.array(
    [
        [1,2],[2,1],[2,3],[3,2],[4,4]
    ]
)

# Defining the Fisher Yates swapping function for the edge set via the consensus group (manual: orbits superfluous)
def edgeFisherYates(inputEdgeSet, extraInfo=True):
    
    # Initializing the edge set and its columns
    edgeSet = np.copy(inputEdgeSet)
    leftColumnEdge = list(edgeSet.T[0])
    rightColumnEdge = list(edgeSet.T[1])
    
    # Printing original state of the edge sets and the vertex indices
    if extraInfo == True:
        print('Initial edge set of the graph:\n', edgeSet)
        print('Target list:\n', leftColumnEdge)
        print('Dual list:\n', rightColumnEdge)
        
    # Looping over the different included endpoints of the target list
    for endpoint in reversed(
        range(
            0, len(leftColumnEdge)-1
        )
    ):
        # Current last point and its dual in the right column
        lastPoint = leftColumnEdge[endpoint]
        dualPoint = rightColumnEdge[endpoint]
        if extraInfo == True:
            print('Current last element: ', lastPoint)
        
        # Randomly selecting points until they satistfy non-degeneracy
        for testIteration in range(
            0, 1000
        ):
        
            # Select a random array element (bounded by included endpoints)
            randomIndex = np.random.randint(0, endpoint+1)
            randomElement = leftColumnEdge[randomIndex]
            dualElement = leftColumnEdge[randomIndex]
            
            # Degeneracy condition
            if (lastPoint != randomElement) and (dualPoint != dualElement):
                if extraInfo == True:
                    print('Satifying element selected!')
                    print('Left edge element', randomElement, 'of index', randomIndex, 'selected.')
                break
            else:
                if extraInfo == True:
                    print('Non-satisfying element selected! Reselecting.')
                
        # Performing the swap with the randomly selected non-degenerate element
        leftColumnEdge[endpoint], leftColumnEdge[randomIndex] = leftColumnEdge[randomIndex], leftColumnEdge[endpoint]
        if extraInfo == True:
            print('Swapped element', randomElement, 'with', lastPoint, end='.\n')
        if extraInfo == True:
            print('New target list state: ', leftColumnEdge)
            
    # Presenting the final state of the target list
    if extraInfo == True:
        print('Final array state: ', leftColumnEdge)
            
    # Gluing back the pieces of the edge set together
    finalEdgeSet = np.column_stack(
        (leftColumnEdge,rightColumnEdge)
    )
    
    # Presenting the final state of the edge set
    if extraInfo == True:
        print('Final state of edge set:\n', finalEdgeSet)
        
    return finalEdgeSet, leftColumnEdge
    
# Performing a test of the new algorithm
edgeFisherYates(testEdgeSet)


# %% Computing probability distribution of group action for consensus Fisher Yates shuffles - コンプリート

# Defining a plotting function for a fixed amount of iterations
def edgeDistribution(shuffleAlgorithm, inputEdgeSet, iterationSize, extraInfo=False):
    
    # Defining the target list
    inputSet = list(
        inputEdgeSet.T[0]
    )
    
    # Defining all possible unique permutations of the input set
    permutationArray = list(
        multiset_permutations(inputSet)
    )
    print('Total possible permutations: ', len(permutationArray))
    print('All possible unique permutations: ', permutationArray)

    # Initialize an empty list to tally up the occurences of given permutations
    tallySet = list(
        np.zeros(
            len(permutationArray), dtype=int
        )
    )
    
    # Iterating through iterations of shuffles
    for iteration in range(1,iterationSize+1):
        
        # Performing a random permutation of the input set
        outputSet = shuffleAlgorithm(inputEdgeSet,False)[1]
        if extraInfo == True:
            print('Permuted set: ',outputSet)
        
        # Checking if it is one of the permutations and if so add to the tally
        for permutation in range(
            0,len(permutationArray)-1
        ):
            if outputSet == permutationArray[permutation]:
                tallySet[permutation] += 1
            
    # Printing output tally set
    if extraInfo == True:           
        print('Final tally: ',tallySet)

    # Plotting results
    permutationIndexSet = list(
        np.arange(
            1, len(permutationArray)+1
        )
    )
    averageOccurence = np.mean(tallySet)/iterationSize

    fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)

    ax = axs[0]
    ax.scatter(permutationIndexSet,np.array(tallySet)/iterationSize, color='magenta',label='Frequency')
    ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average Probability')
    ax.axhline(y=1/len(permutationArray), color='gray', label = 'Expected Average Probability', linestyle = 'dotted')
    ax.set_ylabel('Permutation Probability')
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax.set_title(f'{iterationSize} Independent Shuffles with {shuffleAlgorithm.__name__}')
    ax.legend()
    ax.grid()
    ax.set_axisbelow(True)

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


# %% Trying again for a larger set, and a trivial set
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

print('--- Large Edge Set ---')
edgeDistribution(edgeFisherYates,largeEdgeSet,10000)
print('--- Trivial Edge Set ---')
edgeDistribution(edgeFisherYates,trivialEdgeSet,10000)


# %% Redefing the cosensus shuffle using Peter's notation

# Defining the consensus shuffle with a deterministic run time
def consensusShuffle(targetEdgeSet, extraInfo=True):
    
    # Initializing the edge set and its columns
    edgeSet = np.copy(targetEdgeSet)
    uColumn = list(edgeSet.T[0]) #\vec{v}
    vColumn = list(edgeSet.T[1]) #\vec{u}
    
    # Extra info: printing the original configuration of the set
    if extraInfo == True:
        print('Initial edge set of the graph:\n', edgeSet)
        print('Target list:\n', uColumn)
        print('Dual list:\n', vColumn)
        
    # Looping over the different endpoints of the unselected elements
    for i in reversed(
        range(
            1, len(uColumn) # Not starting at 0 because the alg is trivial for last element
        )
    ):
        # Defining the current ith endpoint of the unselected elements of U
        lastPoint = uColumn[i]
        dualLastPoint = vColumn[i]
        
        # Extra info: printing current selected endpoint
        if extraInfo == True:
            print('Current endpoint: ', lastPoint)
        
        # Initializing the transition set
        t = []
        
        # Constructing the transition set based on non-degenerate elements
        for k in range(
            0, i
            ):
            
            # Defining temporary jth elements in U and V columns
            kthPoint = uColumn[k]
            dualKthPoint = vColumn[k]
            
            # Appending non-degenerate points to the transition set
            if (lastPoint != kthPoint) and (dualLastPoint != dualKthPoint):
                t.append(kthPoint)
                
        # Extra info: printing the transition set
        if extraInfo == True:
            print('Current transition set: ', t)        
                
        # Randomly selecting a point in the transition set and swapping elements
        j = random.choice(t)
        jIndex = uColumn.index(j)
        uColumn[i], uColumn[jIndex] = uColumn[jIndex], uColumn[i]
        
        # Extra info: printing randomly selected element
        if extraInfo == True:
            print('Selected transition point: ', j)
            print('Selected point index in U: ', jIndex)
        
        # Extra info: printing swapped elements and new list
        if extraInfo == True:
            print('Swapped element', uColumn[i], 'with', uColumn[jIndex])
            print('Current target list: ', uColumn)
            print('Current dual list: ', vColumn)
        
    # Gluing back the pieces of the edge set together 
    finalEdgeSet = np.column_stack(
        (uColumn,vColumn)
    )
    
    # Extra info: presenting the final state of the edge set
    if extraInfo == True:
        print('Final state of edge set:\n', finalEdgeSet)
        
    return finalEdgeSet, uColumn
                

# %% Computing the probability distribution for different edge sets
print('--- Test Edge Set ---')
edgeDistribution(consensusShuffle,testEdgeSet,100000)
# print('--- Large Edge Set ---')
# edgeDistribution(consensusShuffle,largeEdgeSet,10000)
print('--- Trivial Edge Set ---')
edgeDistribution(consensusShuffle,trivialEdgeSet,100000)


# %%

