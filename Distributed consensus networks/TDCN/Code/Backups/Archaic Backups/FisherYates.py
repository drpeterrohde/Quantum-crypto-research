#%% Importing modules - コンプリート

# Standard mathematics modules
import numpy as np
import matplotlib.pyplot as plt

# Group theoretic modules
from sympy.utilities.iterables import multiset_permutations
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup
# Notes: consensus group + uniformity


#%% Defining the modern Fisher Yates shuffle algorithm - コンプリート

# Defining the Fisher Yates swapping function
def FisherYates(inputArray,extraInfo=True):
    
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


# %% Computing probability distribution of group action: manual input - コンプリート

# Defining the input set of which the group acts on
inputSet = [1,2,3]

# Roughly for the time being we write all possible permutations in an array
permutationArray = np.array(
    [
        [1,2,3],[2,1,3],[2,3,1],[3,2,1],[1,3,2],[3,1,2]
    ]
)

# Initialize an empty list to tally up the occurences of given permutations
tallySet = [0,0,0,0,0,0]

# Iterating through 100000 permutations
permutationSize = 100000
for iteration in range(1,permutationSize+1):
    
    # Performing a random permutation of the input set
    outputSet = FisherYates(inputSet,False)
    print('Permuted set: ',outputSet)
    
    # Checking if it is one of the permutations and if so add to the tally
    for permutation in range(
        len(permutationArray)
    ):
        if outputSet == list(permutationArray[permutation]):
            tallySet[permutation] += 1
         
# Printing output tally set           
print('Final tally: ',tallySet)

# Plotting results
permutationIndexSet = [1,2,3,4,5,6]
averageOccurence = np.mean(tallySet)/permutationSize

fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)

ax = axs[0]
ax.scatter(permutationIndexSet,np.array(tallySet)/permutationSize, color='magenta',label='Frequency')
ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average')
ax.axhline(y=1/6, color='gray', label = 'Expected Average', linestyle = 'dotted')
ax.set_ylabel('Permutation Probability')
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.set_title('{} Permutations'.format(int(permutationSize)))
ax.legend()
ax.grid()
ax.set_axisbelow(True)

ax = axs[1]
ax.scatter(permutationIndexSet,np.abs(
    ( np.array(tallySet)/permutationSize ) - averageOccurence
), color ='aqua', label='Normalized Residues')
ax.set_xlabel('Unique Permutations')
ax.set_ylabel('Variance')
ax.grid()
ax.set_axisbelow(True)

    
# %% Computing probability distribution of group action: automatic input - コンプリート

# Defining the input set of which the group acts on
inputSet = [1,2,3]

# Defining all possible unique permutations of the input set
permutationArray = list(
    multiset_permutations(inputSet)
)

# Initialize an empty list to tally up the occurences of given permutations
tallySet = list(
    np.zeros(
        len(permutationArray), dtype=int
    )
)

# Iterating through 100000 permutations
permutationSize = 100000
for iteration in range(1,permutationSize+1):
    
    # Performing a random permutation of the input set
    outputSet = FisherYates(inputSet,False)
    print('Permuted set: ',outputSet)
    
    # Checking if it is one of the permutations and if so add to the tally
    for permutation in range(
        len(permutationArray)
    ):
        if outputSet == permutationArray[permutation]:
            tallySet[permutation] += 1
         
# Printing output tally set           
print('Final tally: ',tallySet)

# Plotting results
permutationIndexSet = list(
    np.arange(
        1, len(permutationArray)+1
    )
)
averageOccurence = np.mean(tallySet)/permutationSize

fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)

ax = axs[0]
ax.scatter(permutationIndexSet,np.array(tallySet)/permutationSize, color='magenta',label='Frequency')
ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average')
ax.axhline(y=1/len(permutationArray), color='gray', label = 'Expected Average', linestyle = 'dotted')
ax.set_ylabel('Permutation Probability')
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.set_title('{} Permutations'.format(int(permutationSize)))
ax.legend()
ax.grid()
ax.set_axisbelow(True)

ax = axs[1]
ax.scatter(permutationIndexSet,np.abs(
    ( np.array(tallySet)/permutationSize ) - averageOccurence
), color ='aqua', label='Normalized Residues')
ax.set_xlabel('Unique Permutations')
ax.set_ylabel('Variance')
ax.grid()
ax.set_axisbelow(True)


#%% Group theoretic framework for generalized Fisher Yates shuffle algorithm (permutation group) - コンプリート

# Defining the ordered version of the input set
inputSet = [0,1,2,3]

# Selecting a random permutation of it which represents the different degrees of the nodes
possiblePermutations = list(
    multiset_permutations(inputSet)
)
permutationIndex = np.random.randint(0,len(possiblePermutations))
print('Selected permutation: ', permutationIndex)
degreeSet = possiblePermutations[permutationIndex]
print('Selected permutation: ', degreeSet)

# Initializing the object in cycle notation
initializedSet = Permutation(degreeSet) # caveat: 0 must be present in the list + must be permuted

# Defining the permutation group (more general than symmetric group) over the initialized set
permutationGroup = PermutationGroup([initializedSet])

# Printing the different orbits of the set elements based on all group actions
for element in range(0,len(degreeSet)):
    print('Orbit of element', degreeSet[element], 'is: ', list(permutationGroup.orbit(element)))
    

#%% Defining the generalized Fisher Yates shuffle algorithm (permutation group)  - コンプリート

# Defining the generalized Fisher Yates swapping function
def generalizedFisherYates(inputSet,extraInfo=True):
    
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

generalizedFisherYates([2,0,1,3])
                       
                       
#%% Defining the generalized Fisher Yates shuffle algorithm (symmetric group)  - コンプリート

# Defining the generalized Fisher Yates swapping function
def symmetricFisherYates(inputArray,extraInfo=True):
    
    # Initializing the set and permutation group with the sympy library
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

symmetricFisherYates([0,1,2,3])


# %% Computing probability distribution of group action (permutation group)  - コンプリート

# Defining the input set of which the group acts on
inputSet = [2,1,0,3]

# Defining all possible unique permutations of the input set
permutationArray = list(
    multiset_permutations(inputSet)
)

# Initialize an empty list to tally up the occurences of given permutations
tallySet = list(
    np.zeros(
        len(permutationArray), dtype=int
    )
)

# Iterating through 100000 permutations
permutationSize = 100000
for iteration in range(1,permutationSize+1):
    
    # Print current iteration inputSet
    print('INITIAL INPUT SET: ', inputSet)
    
    # Performing a random permutation of the input set
    outputSet = generalizedFisherYates(inputSet,True)
    print('Permuted set: ',outputSet)
    
    # Checking if it is one of the permutations and if so add to the tally
    for permutation in range(
        len(permutationArray)
    ):
        if outputSet == permutationArray[permutation]:
            tallySet[permutation] += 1
         
# Printing output tally set           
print('Final tally: ',tallySet)

# Plotting results
permutationIndexSet = list(
    np.arange(
        1, len(permutationArray)+1
    )
)
averageOccurence = np.mean(tallySet)/permutationSize

fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)

ax = axs[0]
ax.scatter(permutationIndexSet,np.array(tallySet)/permutationSize, color='magenta',label='Frequency')
ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average')
ax.axhline(y=1/len(permutationArray), color='gray', label = 'Expected Average', linestyle = 'dotted')
ax.set_ylabel('Permutation Probability')
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.set_title('{} Permutations'.format(int(permutationSize)))
ax.legend()
ax.grid()
ax.set_axisbelow(True)

ax = axs[1]
ax.scatter(permutationIndexSet,np.abs(
    ( np.array(tallySet)/permutationSize ) - averageOccurence
), color ='aqua', label='Normalized Residues')
ax.set_xlabel('Unique Permutations')
ax.set_ylabel('Variance')
ax.grid()
ax.set_axisbelow(True)



# %% Computing probability distribution of group action (symmetric group)  - コンプリート

# Defining the input set of which the group acts on
inputSet = [0,1,2,3,4]

# Defining all possible unique permutations of the input set
permutationArray = list(
    multiset_permutations(inputSet)
)

# Initialize an empty list to tally up the occurences of given permutations
tallySet = list(
    np.zeros(
        len(permutationArray), dtype=int
    )
)

# Iterating through 100000 permutations
permutationSize = 100000
for iteration in range(1,permutationSize+1):
    
    # Performing a random permutation of the input set
    outputSet = symmetricFisherYates(inputSet,False)
    print('Permuted set: ',outputSet)
    
    # Checking if it is one of the permutations and if so add to the tally
    for permutation in range(
        len(permutationArray)
    ):
        if outputSet == permutationArray[permutation]:
            tallySet[permutation] += 1
            
         
# Printing output tally set           
print('Final tally: ',tallySet)

# Plotting results
permutationIndexSet = list(
    np.arange(
        1, len(permutationArray)+1
    )
)
averageOccurence = np.mean(tallySet)/permutationSize

fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)

ax = axs[0]
ax.scatter(permutationIndexSet,np.array(tallySet)/permutationSize, color='magenta',label='Frequency')
ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average')
ax.axhline(y=1/len(permutationArray), color='gray', label = 'Expected Average', linestyle = 'dotted')
ax.set_ylabel('Permutation Probability')
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.set_title('{} Permutations'.format(int(permutationSize)))
# ax.set_yscale('log')
ax.legend()
ax.grid()
ax.set_axisbelow(True)

ax = axs[1]
ax.scatter(permutationIndexSet,np.abs(
    ( np.array(tallySet)/permutationSize ) - averageOccurence
), color ='aqua', label='Normalized Residues')
ax.set_xlabel('Unique Permutations')
ax.set_ylabel('Variance')
# ax.set_yscale('log')
ax.grid()
ax.set_axisbelow(True)



#%% Generalized Fisher Yates shuffle (permutation group) with orbit probabilities - コンプリート

# Defining the generalized Fisher Yates swapping function
def orbitFisherYates(inputSet,extraInfo=True):
    
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
        print('FINAL inverseOrbitSizes: ', inverseOrbitSizes)
        print('FINAL PERMUTATION PROBABILITY: ', permutationProbability)
        
    return inputArray, permutationProbability

orbitFisherYates([2,0,1,3])

# %% Computing probability distribution (permutation group) with orbit probabilities  - コンプリート

# Defining the input set of which the group acts on
inputSet = [2,1,0]

# Defining all possible unique permutations of the input set
permutationArray = list(
    multiset_permutations(inputSet)
)

# Initialize an empty list to tally up the occurences of given permutations
tallySet = list(
    np.zeros(
        len(permutationArray), dtype=int
    )
)

# Initialize an empty list of all permutation probabilities
probabilitySet = list(
    np.zeros(
        len(permutationArray), dtype=int
    )
)

# Iterating through 100000 permutations
permutationSize = 50000
for iteration in range(1,permutationSize+1):
    
    # Print current iteration inputSet
    print('INITIAL INPUT SET: ', inputSet)
    
    # Performing a random permutation of the input set
    fisherOutput = orbitFisherYates([2,1,0],False)
    outputSet = fisherOutput[0]
    print('Permuted set: ',outputSet)
    
    # Checking if it is one of the permutations and if so add to the tally
    for permutation in range(
        len(permutationArray)
    ):
        if outputSet == permutationArray[permutation]:
            tallySet[permutation] += 1
            probabilitySet[permutation] += fisherOutput[1]
            
         
# Printing output tally set           
print('Final tally: ',tallySet)

# Plotting results
permutationIndexSet = list(
    np.arange(
        1, len(permutationArray)+1
    )
)
averageOccurence = np.mean(tallySet)/permutationSize

# Printing unormalized added permutation probabilities
print('UNORMALIZED PROBABILITY SET: ', probabilitySet)

# Computed the predicted occurences based on inverse probabilities
for i in range(
        len(permutationArray)
    ):
        probabilitySet[i] = (probabilitySet[i]/(tallySet[i]+0.0000000000000001))

# Printing normalized probabilities for each unique permutation
print('PROBABILITY SET: ', probabilitySet)

fig, axs = plt.subplots(2, 1, figsize=(10, 5), constrained_layout=True)

ax = axs[0]
ax.scatter(permutationIndexSet,np.array(tallySet)/permutationSize, color='magenta',label='Frequency')
ax.axhline(y=averageOccurence, color='black', label = 'Normalized Average')
ax.scatter(permutationIndexSet,probabilitySet, color='gray', label = 'Expected Averages', linestyle = 'dotted')
ax.set_ylabel('Permutation Probability')
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.set_title('{} Permutations'.format(int(permutationSize)))
# ax.set_yscale('log')
ax.legend()
ax.grid()
ax.set_axisbelow(True)

ax = axs[1]
ax.scatter(permutationIndexSet,np.abs(
    ( np.array(tallySet)/permutationSize ) - averageOccurence
), color ='aqua', label='Normalized Residues')
ax.set_xlabel('Unique Permutations')
ax.set_ylabel('Variance')
# ax.set_yscale('log')
ax.grid()
ax.set_axisbelow(True)


#%% Generalized non-degenerate Fisher Yates shuffle (permutation group) with orbit probabilities - コンプリート

# Defining the generalized Fisher Yates swapping function
def orbitFisherYates(inputSet,extraInfo=True):
    
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
            
        # Look at the orbit (from the stabilizer subgroup) of the last element of the list
        stabilizerSubGroup = permutationGroup.stabilizer(lastElement)
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
        print('FINAL inverseOrbitSizes: ', inverseOrbitSizes)
        print('FINAL PERMUTATION PROBABILITY: ', permutationProbability)
        
    return inputArray, permutationProbability

orbitFisherYates([2,0,1,3])

# %% Symmetric non-degenerate with orbit

def nonDegenerateSymmetricFisherYates(inputSet,extraInfo=True):
    
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

nonDegenerateSymmetricFisherYates([2,0,1,3])


# %%


# %%


# %%


# %%


# %% CODE GRAVEYARD - デッドコード

# TESTING ARRAY

# testArray = ['a','b','c','d','e','f']

# print(testArray[0])
# print(testArray[4])

# # Looping over the inclusion of the ends of the array
# print("Original array", testArray)
# for i in reversed(
#     range(
#         1, len(testArray)
#     )
# ):
#     #  Select a random position bounded by the included array elements|
#     print("Current index",i)
#     randomInteger = np.random.randint(0,i+1)
#     randomSelectedIndex = testArray[randomInteger]
#     print("Random selection", randomSelectedIndex)
    
#     # Swapping that element
#     testArray[randomInteger], testArray[i] = testArray[i], testArray[randomInteger]
#     print('Modified array after swapping', testArray[i], 'with', testArray[randomInteger],':', testArray)
    
# print('Final array', testArray)
# print('Cycle array', np.array((['a','b','c','d','e','f']
# ,testArray)))

# OMNIDIRECTIONAL SHUFFLE

# # Defining a test array
# testArray = ['a','b','c','d','e','f']

# # Defining the reversed-direction Fisher Yates swapping function
# def FisherYatesReverse(inputArray,extraInfo=True):
    
#     # Printing the original state of the array
#     if extraInfo == True:
#         print('Initial array state: ', inputArray)
    
#     # Looping over the different included endpoints of the array
#     for endpoint in range(
#             0, len(inputArray)-1
#         ):
#         # Select a random array element (bounded by included endpoints)
#         randomIndex = np.random.randint(endpoint, len(inputArray))
#         randomElement = inputArray[randomIndex]
#         if extraInfo == True:
#             print('Array element', randomElement, 'of index', randomIndex, 'selected.')
            
#         # Swapping the randomly selected element with the current array endpoint
#         if extraInfo == True:
#             print('Swapped element', randomElement, 'with', inputArray[endpoint], end='.\n')
#         inputArray[randomIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomIndex]
#         if extraInfo == True:
#             print('New array state: ', inputArray)
            
#     # Presenting the final state of the array
#     if extraInfo == True:
#         print('Final array state: ', inputArray)
        
#     return inputArray

# # Defining the omnidirectional Fisher Yates  swapping function that randomly selects the cycle direction
# def dualFisherYates(inputArray,extraInfo=True):
    
#     # Printing the original state of the array
#     if extraInfo == True:
#         print('Initial array state: ', inputArray)
        
#     # Randomly determining the cycle direction
#     randomDirection = np.random.randint(0,101)
#     if randomDirection > 50:
#         rightDirection = True
#         if extraInfo == True:
#             print('Regular direction chosen.')
#     else:
#         rightDirection = False
#         if extraInfo == True:
#             print('Reversed direction chosen.')
        

#     # Normal Fisher Yates direction
#     if rightDirection == True:
        
#         # Looping over the different included endpoints of the array
#         for endpoint in reversed(
#             range(
#                 1, len(inputArray)
#             )
#         ):
#             # Select a random array element (bounded by included endpoints)
#             randomIndex = np.random.randint(0, endpoint+1)
#             randomElement = inputArray[randomIndex]
#             if extraInfo == True:
#                 print('Array element', randomElement, 'of index', randomIndex, 'selected.')
                
#             # Swapping the randomly selected element with the current array endpoint
#             if extraInfo == True:
#                 print('Swapped element', randomElement, 'with', inputArray[endpoint], end='.\n')
#             inputArray[randomIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomIndex]
#             if extraInfo == True:
#                 print('New array state: ', inputArray)
                
#     # Reversed Fisher Yates direction
#     if rightDirection == False:
        
#         # Looping over the different included endpoints of the array
#         for endpoint in range(
#                 0, len(inputArray)-1
#             ):
#             # Select a random array element (bounded by included endpoints)
#             randomIndex = np.random.randint(endpoint, len(inputArray))
#             randomElement = inputArray[randomIndex]
#             if extraInfo == True:
#                 print('Array element', randomElement, 'of index', randomIndex, 'selected.')
                
#             # Swapping the randomly selected element with the current array endpoint
#             if extraInfo == True:
#                 print('Swapped element', randomElement, 'with', inputArray[endpoint], end='.\n')
#             inputArray[randomIndex], inputArray[endpoint] = inputArray[endpoint], inputArray[randomIndex]
#             if extraInfo == True:
#                 print('New array state: ', inputArray)
            
#     # Presenting the final state of the array
#     if extraInfo == True:
#         print('Final array state: ', inputArray)
        
#     return inputArray
# %%
