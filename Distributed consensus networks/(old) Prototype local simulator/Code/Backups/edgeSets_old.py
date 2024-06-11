#%% Importing modules - コンプリート

# Standard mathematics modules
import numpy as np
import matplotlib.pyplot as plt


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


# %% Redefing the cosensus shuffle using Peter's notation - コンプリート

# Defining the consensus shuffle with a deterministic run time
def consensusShuffle(targetEdgeSet, extraInfo=True):
    
    # Initializing the edge set and its columns
    edgeSet = np.copy(targetEdgeSet)
    uColumn = list(edgeSet.T[0]) #\vec{u}
    vColumn = list(edgeSet.T[1]) #\vec{v}
    
    # Extra info: printing the original configuration of the set
    if extraInfo == True:
        print('Initial edge set of the graph:\n', edgeSet)
        print('Target list:\n', uColumn)
        print('Dual list:\n', vColumn)
        
    # Looping over the different endpoints of the unselected elements
    for i in reversed(
        range(
            1, len(uColumn)
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
            0, i+1
            ):
            
            # Defining temporary jth elements in U and V columns
            kthPoint = uColumn[k]
            dualKthPoint = vColumn[k]
            
            # Appending non-degenerate points to the transition set
            if (lastPoint != kthPoint) and (dualLastPoint != dualKthPoint):
                t.append(k)
                
        # Extra info: printing the transition set
        if extraInfo == True:
            print('Current transition set: ', t)        
                
        # Randomly selecting a point in the transition set and swapping elements
        j = np.random.choice(t)
        uColumn[i], uColumn[j] = uColumn[j], uColumn[i]
        
        # Extra info: printing randomly selected element
        if extraInfo == True:
            print('Selected transition point: ', j)
            print('Selected point index in U: ', j)
        
        # Extra info: printing swapped elements and new list
        if extraInfo == True:
            print('Swapped element', uColumn[i], 'with', uColumn[j])
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
                

# %% Testing out on different edge sets - コンプリート

# Testing the function on the trivial edge set
consensusShuffle(trivialEdgeSet)


# %%
