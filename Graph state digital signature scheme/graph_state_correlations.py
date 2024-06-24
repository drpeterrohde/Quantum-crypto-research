import networkx as nx
import random

def graph_simulation(msg_bits, msg_qubit_connections, graph_size):
    #we first generate a random graph of size graph_size according to the Erdos Reyni G_n,p model
    #We set p = 1/2 (probability an edge connects two nodes)
    random_graph = nx.erdos_renyi_graph(graph_size,float(1/graph_size),457,False) #change the seed around when testing
    
    #add message qubit node pairs to the graph
    #each 
    for i in range(msg_bits):
        random_graph.add_node('Z_%s' % i)
        for j in range(msg_qubit_connections):
            k = random.randrange(0,graph_size - 1) #technically I could be repeating an edge, but this should happen with low probability
            random_graph.add_edge('Z_%s' % i, k)
        
        random_graph.add_node('Y_%s' % i)

        for j_prime in range(msg_qubit_connections):
            ell = random.randrange(0,graph_size - 1)
            random_graph.add_edge('Y_%s' % i, ell)
        
    #count the number of nodes whose neighborhoods have nodes which will be measured by Y
    good_measurements = 0

    for s in range(graph_size):
        Z_neighbor = False
        neighborhood = list(random_graph.adj[s])
        for t in range(len(neighborhood)): #check if node itself is measured with Z
            if(isinstance(neighborhood[t], str)):
                if(neighborhood[t][0] == 'Z'):
                    Z_neighbor = True
                    break
            if(Z_neighbor == False):
                neighborhood_of_neighbor = list(random_graph.adj[neighborhood[t]])
                for y in range(len(neighborhood_of_neighbor)): #now check if any node in the neighborhood is measured with Z
                    if(isinstance(neighborhood_of_neighbor[y], str)):
                        if(neighborhood_of_neighbor[y][0] == 'Z'):
                            Z_neighbor = True
                            break
        if Z_neighbor == False:
            good_measurements += 1          
    print(good_measurements) #number of nodes whose neighborhood has only Y measurements
            

#A test graph. I basically copy paste the code in my function below and apply it to this test graph

# G = nx.Graph()
# for i in range(0,8):
#     G.add_node(i)

# G.add_node('Z_%s' % 0)
# G.add_node('Y_%s' % 0)
# G.add_node('Z_%s' % 1)
# G.add_node('Y_%s' % 1)
# G.add_node('Z_%s' % 2)
# G.add_node('Y_%s' % 2)

# G.add_edge('Z_%s' % 0, 2)
# G.add_edge('Z_%s' % 0, 0)
# G.add_edge('Y_%s' % 0, 3)
# G.add_edge('Y_%s' % 0, 5)
# G.add_edge('Z_%s' % 1, 0)
# G.add_edge('Z_%s' % 1, 5)
# G.add_edge('Y_%s' % 1, 2)
# G.add_edge('Y_%s' % 1, 6)
# G.add_edge('Z_%s' % 2, 3)
# G.add_edge('Z_%s' % 2, 6)
# G.add_edge('Y_%s' % 2, 5)
# G.add_edge('Y_%s' % 2, 6)

# G.add_edge(0,1)
# G.add_edge(0,3)
# G.add_edge(1,7)
# G.add_edge(2,3)
# G.add_edge(4,6)
# G.add_edge(5,6)


# good_measurements = 0

# for s in range(8):
#     Z_neighbor = False
#     neighborhood = list(G.adj[s])
#     for t in range(len(neighborhood)): #check if node itself is measured with Z
#         if(isinstance(neighborhood[t], str)):
#             if(neighborhood[t][0] == 'Z'):
#                 Z_neighbor = True
#                 break
#         if(Z_neighbor == False):
#             neighborhood_of_neighbor = list(G.adj[neighborhood[t]])
#             for y in range(len(neighborhood_of_neighbor)): #now check if any node in the neighborhood is measured with Z
#                 if(isinstance(neighborhood_of_neighbor[y], str)):
#                     if(neighborhood_of_neighbor[y][0] == 'Z'):
#                         Z_neighbor = True
#                         break
#     if Z_neighbor == False:
#         print(s)
#         good_measurements += 1          
# print(good_measurements)




    
graph_simulation(3,2,500)
