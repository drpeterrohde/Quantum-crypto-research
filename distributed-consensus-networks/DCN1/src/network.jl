function Network()
    network_nodes_data = read("network_nodes.json", String)
    network_nodes_json = JSON3.read(network_nodes_data)

    this_public_keys = network_nodes_json.public_keys
    this_public_key_hashes = map(x -> hash(x), this_public_keys)

    network_policy_data = read("network_policy.json", String)
    network_policy_json = JSON3.read(network_policy_data)

    this_hearbeat_period = network_policy_json.heartbeat_period
    this_protocol_steps = network_policy_json.protocol_steps
    this_network_policy = NetworkPolicy(this_hearbeat_period, this_protocol_steps)

    new(this_network_policy, this_public_keys, this_public_key_hashes)
end

function get_current_heartbeat(network_policy::NetworkPolicy)
    now::Time = time_ns()
    heartbeat::Int64 = div(now, network_policy.heartbeat_period)
    round::Int64 = div(heartbeat, network_policy.protocol_steps)
    return (heartbeat, round)
end

function get_next_heartbeat_time(network_policy::NetworkPolicy)::Tuple{Time, Time}
    (this_heartbeat, this_round) = get_current_heartbeat(network_policy)

    next_heartbeat_time::Time = (this_heartbeat + 1) * network_policy.heartbeat_period
    next_round_time::Time = (this_round + 1) * (network_policy.heartbeat_period * network_policy.protocol_steps)

    return (next_heartbeat_time, next_round_time)
end

function sleep_until(target_time_ns::Time)
    current_time_ns = time_ns()
    if target_time_ns > current_time_ns
        sleep_duration_s = (target_time_ns - current_time_ns) / 1e9
        sleep(sleep_duration_s)
    end
end

function make_dummy_network(num_nodes::Int64)
    network_policy_data = Dict("heartbeat_period" => 1e7, "protocol_steps" => 4)
    network_policy_json = JSON3.write(network_policy_data)
    open("config/network_policy.json", "w") do f
        write(f, network_policy_json)
    end

    public_keys = Vector{PublicKey}()
    private_keys = Vector{PrivateKey}()
    sockets = Vector{SocketAddr}()

    for i in 1:num_nodes
        keypair = KeyPair()
        push!(public_keys, keypair.public_key)
        push!(private_keys, keypair.private_key)
        sock = SocketAddr("127.0.0.1", 8000 + i)
        push!(sockets, sock)
    end

    network_nodes_data = Dict("public_keys" => public_keys, "sockets" => sockets)
    network_nodes_json = JSON3.write(network_nodes_data)
    open("config/network_nodes.json", "w") do f
        write(f, network_nodes_json)
    end

    for i in 1:num_nodes
        node_data = Dict("private_key" => private_keys[i], "public_key" => public_keys[i], "socket" => sockets[i])
        node_data_json = JSON3.write(node_data)
        open("config/node_config_$i.json", "w") do f
            write(f, node_data_json)
        end
    end
end