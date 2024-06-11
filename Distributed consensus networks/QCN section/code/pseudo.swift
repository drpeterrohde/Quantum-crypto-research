import Foundation

struct ProofOfConsensus {
    var networkState: NetworkState
}

struct NetworkState {
    var constitution: Data // Constitution description
    var proposal: Data // Proposed constitution update
    var nodes: [Data] // Array of nodes' public keys 
}