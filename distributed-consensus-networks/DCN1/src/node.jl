function Node(index::Int64)
    # Node config (node_config_n.json)
    config_filename = "config/node_config_$(string(index)).json"
    config_json_string = read(config_filename, String)
    config_data = JSON3.read(config_json_string)

    my_public_key::PublicKey = config_data.public_key
    my_private_key::PrivateKey = config_data.private_key
    my_keypair::KeyPair = KeyPair(public_key=my_public_key, private_key=my_private_key)
    my_socket::SocketAddr = SocketAddr(config_data.socket.ip, config_data.socket.port)

    # Newtwork nodes (network_nodes.json)
    network_nodes_filename = "config/network_nodes.json"
    network_nodes_json_string = read(network_nodes_filename, String)
    network_nodes_data = JSON3.read(network_nodes_json_string)

    my_network_node_public_keys::Vector{PublicKey} = network_nodes_data.public_keys

    my_network_node_sockets = Vector{SocketAddr}()
    for sock in network_nodes_data.sockets
        push!(my_network_node_sockets, SocketAddr(sock.ip, sock.port))
    end

    my_network_node_ids = map(x -> hash(string(x)), my_network_node_public_keys)
    my_id = hash(string(my_keypair.public_key))

    my_ip_address = IPv4(my_socket.ip)
    my_ip_port = my_socket.port

    Node(my_id, my_keypair, 
        Vector{Message}(),
        my_ip_address, my_ip_port, UDPSocket(),
        my_network_node_ids, my_network_node_public_keys, my_network_node_sockets,
        NetworkPolicy(), ReentrantLock(), Atomic{Bool}(false))
end

function get_protocol_bid(node::Node, round::Int64)::String
    # println("Node $(short_fingerprint(node.id)): BID")
    dummy_bid = hash([String(deepcopy(node.id)), string(time_ns())])
    bid_dict = Dict("type" => "BID", "round" => round, "step" => 1, "bid" => dummy_bid)
    bid_data::String = JSON3.write(bid_dict)
    return bid_data
end

function execute_next_protocol_round(node::Node)
    println("Node $(short_fingerprint(node.id)): Execute round")
    (hearbeat, round) = get_current_heartbeat(node.network_policy)
    (next_heartbeat_time, next_round_time) = get_next_heartbeat_time(node.network_policy)
    next_round = round + 1

    step_1_time::Time = next_round_time
    step_2_time::Time = step_1_time + node.network_policy.heartbeat_period
    step_3_time::Time = step_2_time + node.network_policy.heartbeat_period
    step_4_time::Time = step_3_time + node.network_policy.heartbeat_period

    # Step 1: BID
    bid_data = get_protocol_bid(node, next_round)
    println("Bid: ", bid_data)
    sleep_until(step_1_time)
    broadcast(node, bid_data)

    # Step 2: ACCEPT
    # sleep_until(step_2_time)
    # println("Node $(short_fingerprint(node.id)): ACCEPT")

    # Step 3: VOTE
    # sleep_until(step_3_time)
    # println("Node $(short_fingerprint(node.id)): VOTE")

    # Step 4: COMPLIANCE
    # sleep_until(step_4_time)
    # println("Node $(short_fingerprint(node.id)): COMPLIANCE")
end

function listen(node::Node)
    println("Node $(lookup_node_id(node,node.id)) listening: ", node.ip_address, ":", node.ip_port)
    while node.alive[]
        addr, data = recvfrom(node.udp_socket)
        time_received = time_ns()
        json_data = JSON3.read(data)
        packet::PacketIn = PacketIn(json_data.sender, json_data.data, json_data.signature, time_received)
        @async process_packet(node, packet)
    end
end

function lookup_node_id(node::Node, node_id::PublicKeyHash)
    index = findfirst(x -> x == node_id, node.network_node_ids)
    return index
end

function process_packet(node::Node, packet::PacketIn)
    index = lookup_node_id(node, packet.sender)
    json_data = JSON3.read(packet.data, Dict{String, Any})
    if index != nothing
        if verify_sig(node, packet)
            verified_message::Message = Message(packet.sender, json_data)
            lock(node.lock) do
                push!(node.messages, verified_message)
            end
        end
    end
end

function start(node::Node)
    # node.udp_socket = UDPSocket()
    bind(node.udp_socket, node.ip_address, node.ip_port)
    atomic_xchg!(node.alive, true) 

    # Background UDP listener thread
    @async listen(node)

    # Execute protocol
    @async execute_next_protocol_round(node)
end

function stop(node::Node)
    atomic_xchg!(node.alive, false) 
    close(node.udp_socket)
    # flush_messages(node)
end

function flush_messages(node::Node)
    lock(node.lock) do
        node.messages = []
    end
end

function get_all_messages(node::Node)::Vector{Message}
    temp_copy::Vector{Message} = []
    lock(node.lock) do
        temp_copy = node.messages
    end
    return temp_copy
end

function get_filtered_messages(node::Node, type::String, round::Int64)::Vector{Message}
    messages = get_all_messages(node)
    filtered::Vector{Message} = []
    for message in messages
        if message.data["round"]==round && message.data["type"]==type
            push!(filtered, message)
        end
    end
    return filtered
end

function broadcast(node::Node, data::String)
    println("Send: ", data)
    signature = sign(data, node.keypair.private_key)
    packet_out = PacketOut(node.id, data, signature)
    json_data = JSON3.write(packet_out)
    for index in 1:length(node.network_node_ids)
        dest_ip = IPv4(node.network_node_sockets[index].ip)
        dest_port = node.network_node_sockets[index].port
        send(node.udp_socket, dest_ip, dest_port, json_data)
    end
end