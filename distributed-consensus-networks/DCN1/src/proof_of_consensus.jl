function verify(poc::ProofOfConsensus)::Bool
    # Are all signatures valid?
    for index in 1:length(network_node_public_keys)
        if accepted_nodes[index] == true
            if !verify_sig(network_node_public_keys, accepts_sigs[index], String(accepted_nodes))
                return false
            end
        end
    end

    # Impose minimum set size

    # establish shared random variable from accept_sigs
    # chi = 
    
    # Are there a majority

    return true
end

function shared_random_source(poc::ProofOfConsensus)
    contributing_hashes::Vector{Hash}()

    for index in 1:length(network_node_public_keys)
        if accepted_nodes[index] == true
            push!(contributing_hashes, poc.accepted_bids[index])
        end
    end

    network_key = hash(contributing_hashes)
    return network_key
end