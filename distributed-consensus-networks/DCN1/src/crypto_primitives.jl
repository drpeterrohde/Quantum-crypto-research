using PyCall

py_crypto_sigs = pyimport("cryptography.hazmat.primitives.asymmetric.ed448")
py_crypto_hash = pyimport("cryptography.hazmat.primitives.hashes")

function KeyPair(;public_key::PublicKey, private_key::PrivateKey)
    KeyPair(public_key, private_key)
end

"""
    generate_keypair()

Return the newly generated `keypair`
"""
function KeyPair()
    private_key_obj = py_crypto_sigs.Ed448PrivateKey.generate()
    public_key_obj = private_key_obj.public_key()

    private_key_str = PrivateKey(private_key_obj.private_bytes_raw())
    public_key_str = PublicKey(public_key_obj.public_bytes_raw())

    keypair = KeyPair(public_key_str, private_key_str)
    return keypair
end

"""
    sign(message, private_key)

Sign `message` using `private_key` and return the `signature`
"""
function sign(data::String, private_key::PrivateKey)::Signature
    data_hash::Hash = hash(data)
    private_key_obj = py_crypto_sigs.Ed448PrivateKey.from_private_bytes(pybytes(private_key))
    signature::Signature = Signature(private_key_obj.sign(pybytes(data_hash)))
    return signature
end

"""
    verify_sig(public_key, signature, data)

Verify the `signature` of `data` against `public_key`. Returns `true` if `signature` is valid.
"""
function verify_sig(public_key::PublicKey, signature::Signature, data::String)::Bool
    public_key_obj = py_crypto_sigs.Ed448PublicKey.from_public_bytes(pybytes(public_key))
    try
        data_hash = hash(data)
        public_key_obj.verify(pybytes(signature), pybytes(data_hash))
        return true
    catch
        return false
    end
end

function verify_sig(node::Node, packet::PacketIn)::Bool
    index = findfirst(x -> x == packet.sender, node.network_node_ids)
    if index != nothing
        return verify_sig(node.network_node_public_keys[index], packet.signature, packet.data)
    else
        return false
    end
end

"""
    hash(data)

Return the `hash` of `data`.
"""
function hash(data::String)::Hash
    digest = py_crypto_hash.Hash(py_crypto_hash.SHA3_256())
    digest.update(pybytes(data))
    hash_out = Hash(digest.finalize())
    return hash_out
end

"""
    hash(messages)

Return the `hash` of the sorted, concatenated array of `messages`.
"""
function hash(data_array::Vector{String})::Hash
    concat_sorted::String = join(sort(data_array))
    hash_out = hash(concat_sorted)
    return hash_out
end

# function verify_sig(public_keys::Vector{PublicKey}, signature::String, data::String)
#     index = findfirst(x -> x.sender == message.sender, public_key_hashes)
#     if index != nothing
#         return verify_sig(public_keys[index], message.signature, message.data)
#     else
#         return false
#     end
# end
