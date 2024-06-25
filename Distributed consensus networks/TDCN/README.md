# Topological-Consensus-Networks
###### Under collaboration with [Dr. Peter Rohde](https://peterrohde.org/) at [BTQ](https://www.btq.com/) technologies and [Professor Gavin Brennen](https://researchers.mq.edu.au/en/persons/gavin-brennen) at [Macquarie University](https://researchers.mq.edu.au/en/).

![alt text](https://github.com/drpeterrohde/Quantum-crypto-research/blob/main/Distributed%20consensus%20networks/TDCN/Plots/3-to-1-point%20network.png?raw=true)

## Objective

Consensus protocols in blockchain transactions suffer from scaling issues
when adopting proof-of-work schemes. These schemes rely on parties competing to solve
cryptographic puzzles for stakes in transactions and are inefficient due to an artificial
reduction in their transaction rate when scaling up networks (to prevent inflation and
multiple winners). Instead, we adopt *proof-of-consensus* schemes whereby autonomous
networks of known parties are quantum randomly allocated into sub-networks to perform
consensus on independent transactions. Such networks have their compliance tested during
consensus and so are known as *consensus networks*. These schemes do not require stakes
in transactions as they instead rely on mutual benefit and do not run into the scaling
inefficiencies of proof-of-work schemes. The security of such a protocol is characterized
by the *trust* between parties in the network (and additionally external clients), a dynamic
quantity that changes over time. We present a *topological* formulation of the dynamics
of trust in closed consensus networks to describe how they evolve in time in an efficient
and generally covariant manner. We compute the intersection of trust between parties in a
network, and the trust as viewed by clients, to define an overall effective trusted network to
be offered as a service. Finally, with the use of algebraic topology and surgery theory, we
present a combinatoric way for networks to autonomously split off and combine with each
other for a natural way to scale up the amount of transactions verified, for more efficiency
overall.

## Code Functionality

This code manipulates and analyzes edge sets in graph theory using NumPy, Matplotlib, and SymPy. It defines three edge sets (testEdgeSet, largeEdgeSet, and trivialEdgeSet). The consensusShuffle function permutes the edges of a given set with a deterministic runtime, selecting and swapping elements iteratively to ensure non-degenerate transitions. The probabilityDistribution function calculates and visualizes permutation probabilities for a given edge set over multiple iterations. It uses SymPy to generate unique permutations and tallies their occurrences post-shuffling. Results are plotted to display permutation probabilities and variance. The code also removes duplicate edge sets using the removeDegeneracy function, converting edge sets to frozensets for uniqueness. The sequenceVerifier function checks if a degree sequence is satisfiable by verifying conservation and boundedness of degrees, breaking the sequence into sub-sequences, and ensuring their sums meet necessary conditions. The edgeAssignment function creates an initial graph assignment from a degree sequence, provided it passes verification. It constructs the edge set by iterating through sequences and decrementing degree values as edges are assigned. Debugging print statements offer insights into the internal states of edge sets and sequences, making the code a useful tool for exploring graph theory concepts and performing permutations and probability analyses on edge sets.


## Caveats

## Next Steps
