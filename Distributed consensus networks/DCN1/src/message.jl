function PacketOut(node::Node, data::Data)
    this_sender = PublicKeyHash(node.id)
    this_data = data
    this_hash = Hash(data)
    this_signature = sign(this_hash, node.keypair.private_key)
    # PacketOut(this_sender, this_data, this_signature)
end

function show(io::IO, obj::Message)
    str =  "Message(sender: $(short_fingerprint(obj.sender)), data: $(string(obj.data)))"
    print(io, str)
end

function show(io::IO, obj::PacketIn)
    str =  "PacketIn(sender: $(short_fingerprint(obj.sender)), signature: $(short_fingerprint(obj.signature)), data: $(String(deepcopy(obj.data))), hash: $(short_fingerprint(hash(obj.data))), time: $(obj.time_received))"
    print(io, str)
end

function show(io::IO, obj::PacketOut)
    str =  "PacketOut(sender: $(short_fingerprint(obj.sender)), signature: $(short_fingerprint(obj.signature)), data: $(String(deepcopy(obj.data))), hash: $(short_fingerprint(hash(obj.data))))"
    print(io, str)
end

function short_fingerprint(data)::String
    return first(String("$(bytes2hex(deepcopy(data)))"), 6)
end
