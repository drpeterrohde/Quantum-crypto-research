const PublicKey = Vector{UInt8}
const PrivateKey = Vector{UInt8}
const Signature = Vector{UInt8}
const PublicKeyHash = Vector{UInt8}
const Hash = Vector{UInt8}
const Bid = Vector{UInt8}
const Data = Vector{UInt8}
const Time = UInt64
# const NetworkState = Vector{UInt8}

abstract type AbstractMessage end

struct SocketAddr
    ip::String
    port::UInt16
end

struct KeyPair
    public_key::PublicKey
    private_key::PrivateKey
end

struct PacketOut <: AbstractMessage
    sender::PublicKeyHash
    data::String
    signature::Signature
end

struct PacketIn <: AbstractMessage
    sender::PublicKeyHash
    data::String
    signature::Signature
    time_received::Time
end

struct Message <: AbstractMessage
    sender::PublicKeyHash
    data::Dict{String, Any}
end

struct NetworkPolicy
    heartbeat_period::Time
    protocol_steps::Int64    
end

mutable struct Node
    id::PublicKeyHash
    keypair::KeyPair
    messages::Vector{Message}
    ip_address::IPAddr
    ip_port::Int16
    udp_socket::UDPSocket
    network_node_ids::Vector{PublicKeyHash}
    network_node_public_keys::Vector{PublicKey}
    network_node_sockets::Vector{SocketAddr}
    network_policy::NetworkPolicy
    lock::ReentrantLock
    alive::Atomic{Bool}
end

struct Network
    network_policy::NetworkPolicy
    public_keys::Vector{PublicKey}
    public_key_hashes::Vector{PublicKeyHash}
end

struct ProofOfConsensus
    network_node_public_keys::Vector{PublicKey}
    accepted_nodes::Vector{Bool}
    accepted_bids::Vector{Bid}
    accept_sigs::Vector{Signature}
    votes::Vector{Bool}
    votes_sigs::Vector{Signature}
end