# using .DCN

include("../src/DCN.jl")

node1 = Node(1)
node2 = Node(2)

start(node1)
start(node2)

println("SLEEP")
sleep(5)

stop(node1)
stop(node2)

println("COMPLETE")
println("Node 1: ", node1.messages)
println("Node 2: ", node2.messages)

