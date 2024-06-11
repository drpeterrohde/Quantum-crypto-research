using Plots
using Crayons
using Random
using StatsBase

function uniform_graph(nodes, deg)
    E=[]
    for i in 1:nodes
        for fan in 0:(deg-1)
            j = mod(i+fan-1,nodes)+1
            e = [i j]
            push!(E,e)
        end    
    end
    return E
end

function uniform_graph_history(nodes, deg)
    E=[]
    history = []
    for i in 1:nodes
        for fan in 0:(deg-1)
            j = mod(i+fan-1,nodes)+1
            e = [i j]
            push!(E,e)
            push!(history, Int64[])
        end
    end
    return E, history
end

function symmetric_group_shuffle(E)
    E = deepcopy(E)
    for i in 1:length(E)
        j = rand(i:length(E))
        E[i][2], E[j][2] = E[j][2], E[i][2]
    end
    return E
end

function consensus_group_shuffle(E)
    edges = deepcopy(E)
    for i in 1:length(edges)
        t = transition_set(edges, i)
        if length(t) > 0
            j = rand(t)
            # First index swap
            edges[i][1], edges[j][1] = edges[j][1], edges[i][1] 
        end
    end
    if !is_simple_graph(edges)
        println(Crayon(foreground=:red), "Error: duplicate edges.")
    end
    return edges
end

function consensus_group_shuffle_orbits(E)
    edges = deepcopy(E)
    traversed_edges = deepcopy(E)

    for i in 1:length(edges)
        t = transition_set_orbits(edges, traversed_edges, i)
        j = rand(t)

        e_1 = [edges[i][1] edges[j][2]]
        e_2 = [edges[j][1] edges[i][2]]

        edges[i][1], edges[j][1] = edges[j][1], edges[i][1] # First index swap

        if i != j
            push!(traversed_edges, e_1)
            push!(traversed_edges, e_2)
        else
            push!(traversed_edges, e_1)
        end
        # println("Traversed edges: ", traversed_edges)
    end
    if !is_simple_graph(edges)
        println(Crayon(foreground=:red), "Error: duplicate edges.")
        println("E    : ", edges)
        println("Etrav: ", traversed_edges)
    end
    return edges
end

function is_simple_graph(E)::Bool
    return length(E) == length(Set(E))
end

function transition_set_orbits(E, E_traversed, i)
    t = [i]

    for j in (i+1):length(E)
        e_1 = [E[i][1] E[j][2]]
        e_2 = [E[j][1] E[i][2]]

        valid_e_1 = e_1 ∉ E_traversed
        valid_e_2 = e_2 ∉ E_traversed

        if valid_e_1 && valid_e_2
            push!(t, j)
        end
    end
    return t
end

function plot_bipartite(nodes, edges)
    x = [zeros(nodes); ones(nodes)]
    y = [collect(1:nodes); collect(1:nodes)]
    labels = text.([1:nodes; 1:nodes])

    p = plot()
    for edge in edges
        plot!([0, 1], [-y[edge[1]], -y[edge[2]]], color=:blue, lw=1, legend=false, showaxis=false, xticks=nothing, yticks=nothing)
    end
    scatter!(x, -y, series_annotations=labels, color=:cyan, markersize=15)
    return p
end

function group_statistics(nodes, deg, iters)
    tally = zeros(Int64, nodes, nodes)

    for iter in 1:iters
        E_init = uniform_graph(nodes, deg)
        E = consensus_group_shuffle_orbits(E_init)
        for e in E
            tally[e[1], e[2]] += 1
        end
    end

    stats = tally / Float64(iters)

    println("Statistics:")
    display(round.(stats; digits=2))
    println()
    for u in 1:nodes
        p = round.(sum(stats[u,:]); digits=3)
        println("u=$u: deg(u)=$deg, p=$p")
    end
    println()
    for v in 1:nodes
        p = round.(sum(stats[:,v]); digits=2)
        println("v=$v: deg(v)=$deg, p=$p")
    end

    return stats
end

# Main

# Uniform bidding
nodes = 5
deg = 2
iters = 1000

group_statistics(nodes, deg, iters)

# edges = uniform_graph(nodes, deg)
# println("Initial edges:")
# display(edges)

# final_edges = consensus_group_shuffle_orbits(edges)
# println("\nFinal edges:")
# display(final_edges)



# edges, history = uniform_graph_history(nodes, deg)
# rand_edges, rand_history = consensus_group_shuffle_history(edges, history)
# fig = plot_bipartite(nodes, rand_edges)
# display(fig)









# DOESN'T WORK
# function random_uniform_graph(nodes::Int64, deg::Int64)
#     E=[]
#     valence = deg * ones(Int64,nodes)
#     println(valence)
#     for i in 1:nodes
#         choices = findall(x -> x > 0, valence)
#         random_perm = shuffle(choices)
#         println("i=$i: choices=$choices")
#         random_subset = random_perm[1:deg]
#         println("rand = $random_subset")
#         for j in random_subset
#             valence[j] -= 1
#             e = [i j]
#             push!(E,e)
#         end
#     end
#     return E
# end

# function initial_graph(degU, degV)
#     valU = sort(deepcopy(degU), rev=true)
#     valV = sort(deepcopy(degV), rev=true)
#     E = []

#     for u in 1:length(valU)
#         if valU[u] > 0
#             for v in 1:length(valV)
#                 if valV[v] > 0
#                     push!(E, [u v])
#                     valU[u] -= 1
#                     valV[v] -= 1
#                 end
#                 if valU[u] == 0
#                     break
#                 end
#             end
#         end
#     end

#     remainder = sum(valU) + sum(valV)
#     if remainder > 0
#         println(Crayon(foreground=:red), "Error: unrealisable graph.")
#         E = []
#     end

#     return E
# end

# function transition_set(E, E_init, i)
#     t = []
#     for j in (i+1):length(E)
#         e_1 = [E[i][1], E[j][2]]
#         e_2 = [E[j][1], E[i][2]]

#         e_fixed = E[1:(i-1)]
#         e_not_fixed = E[i:length(E)]

#         valid_e_1 = (e_1 ∉ e_fixed)
#         valid_e_2 = (e_2 ∉ E_init)

#         valid_swap = ((E[i][1] != E[j][1]) && (E[i][2] != E[j][2]))

#         if valid_swap && valid_e_1 && valid_e_2
#             push!(t, j)
#         end
#     end
#     return t
# end