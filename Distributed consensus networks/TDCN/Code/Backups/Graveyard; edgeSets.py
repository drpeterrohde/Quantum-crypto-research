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