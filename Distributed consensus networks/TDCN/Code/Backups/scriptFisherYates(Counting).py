#%% Importing modules - コンプリート

# Standard mathematics modules
import numpy as np
import matplotlib.pyplot as plt

# Group theoretic modules
from sympy.utilities.iterables import multiset_permutations
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import (SymmetricGroup, CyclicGroup, DihedralGroup)
# Notes: manual + random


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


# %%% Computing how many selected permutations after removing degeneracy for general network size of n



#%% Manually defining the Fisher Yates shuffles with orbit probabilities under the consensus group (symmetric group modulo degeneracies) - コンプリート

# Defining the generalized orbit Fisher Yates swapping function (G = symmetric)
def consensusFisherYates(inputSet,extraInfo=True):
    
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


# %%
