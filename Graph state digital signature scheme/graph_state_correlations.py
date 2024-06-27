import networkx as nx
import random

def graph_simulation_graph_nbhds(msg_bits, msg_qubit_connections, graph_size):
    #we first generate a random graph of size graph_size according to the Erdos Reyni G_n,p model
    #We set p = 1/n (probability an edge connects two nodes)
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

def form_random_msg_qubit_neighbors(degree_param, msg_bits, graph_size): #starts with an empty graph of size graph_size. Then forms message qubit pairs (Z,Y) and randomly connects each qubit node with degree_param many graph nodes.
    n = graph_size
    G = nx.empty_graph(n)

    for i in range(msg_bits):
        vertex_set_Z = set()
        vertex_set_Y = set()
        G.add_node('Z_%s' % i)
        for j in range(degree_param):
            k = random.randrange(0,graph_size - 1)
            if k not in vertex_set_Z: 
                G.add_edge('Z_%s' % i, k)
                vertex_set_Z.add(k)
        
        G.add_node('Y_%s' % i)
        for j_prime in range(degree_param):
            ell = random.randrange(0,graph_size - 1)
            if ell not in vertex_set_Y: 
                G.add_edge('Y_%s' % i, ell)
                vertex_set_Y.add(ell)
    return [G, vertex_set_Z]

def local_complementation(graph, vertex):  #function for computing local complements around a vertex
    vertex_neighborhood = list(graph.adj[vertex])
    for u in vertex_neighborhood:
        for v in vertex_neighborhood:
            if graph.has_edge(u,v):
                graph.remove_edge(u,v)
            else:
                graph.add_edge(u,v)
def procedure(degree_param, msg_bits, graph_size, number_of_iterations):
    simul = form_random_msg_qubit_neighbors(degree_param, msg_bits, graph_size)
    G = simul[0]
    z_set = simul[1]
    vertex_set = set(range(graph_size))
    not_z_set = vertex_set.difference(z_set) #gets all vertices in the graph not measured with Z

    for n in range(number_of_iterations):
        for v in not_z_set:
            local_complementation(G, v)
    
    print(G.number_of_edges())


procedure(2,3,50,4)

# def graph_simulation_msg_qubit_nbhds(msg_bits, msg_qubit_connections, graph_size):
#     #we first generate a random graph of size graph_size according to the Erdos Reyni G_n,p model
#     #We set p = 1/n (probability an edge connects two nodes)
#     random_graph = nx.erdos_renyi_graph(graph_size,float(1/graph_size),457,False) #change the seed around when testing
    
#     #add message qubit node pairs to the graph
#     #keep track of the message qubit nodes
#     #Z_msg_qubit_nodes = [] 
#     Z_measurements = set()
#     for i in range(msg_bits):
#         random_graph.add_node('Z_%s' % i)
#         #Z_msg_qubit_nodes.append('Z_%s'% i) #easy to reference these nodes later
#         for j in range(msg_qubit_connections):
#             k = random.randrange(0,graph_size - 1) #technically I could be repeating an edge, but this should happen with low probability
#             random_graph.add_edge('Z_%s' % i, k)
#             Z_measurements.add(k)
        

        
#         random_graph.add_node('Y_%s' % i)
#         #msg_qubit_nodes.append('Y_%s' % i)
#         for j_prime in range(msg_qubit_connections):
#             ell = random.randrange(0,graph_size - 1)
#             random_graph.add_edge('Y_%s' % i, ell)
    
#     return graph_size - len(Z_measurements) #number of graph qubits which either only Y measured or not measured at all



#print(graph_simulation_msg_qubit_nbhds(3,2,8)) #example to play around with


    

