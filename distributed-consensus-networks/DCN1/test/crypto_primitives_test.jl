using Term
using Term.TermMarkdown
import Term: tprint, tprintln
using Markdown

# using .DCN
include("../src/DCN.jl")

tprintln(md"# DCN cryptographic primitives tests")
println(@underline @blue @italic "[crypto_primitives.jl]\n")

keypair_A = KeyPair()
public_key_hash_A = hash(string(keypair_A.public_key))
println("Keypair (Alice):")
println("\tPublic key ($(length(keypair_A.public_key)) bytes): ", first(bytes2hex(keypair_A.public_key), 16), "...")
println("\tPublic key hash ($(length(public_key_hash_A)) bytes): ", first(bytes2hex(public_key_hash_A), 16), "...")
println("\tPrivate key ($(length(keypair_A.private_key)) bytes): ", first(bytes2hex(keypair_A.private_key), 16), "...")
println()

keypair_B = KeyPair()
public_key_hash_B = hash(string(keypair_B.public_key))
println("Keypair (Bob):")
println("\tPublic key ($(length(keypair_B.public_key)) bytes): ", first(bytes2hex(keypair_B.public_key), 16), "...")
println("\tPublic key hash ($(length(public_key_hash_B)) bytes): ", first(bytes2hex(public_key_hash_B), 16), "...")
println("\tPrivate key ($(length(keypair_B.private_key)) bytes): ", first(bytes2hex(keypair_B.private_key), 16), "...")
println()

message_1 = "hello world"
message_2 = "goodbye world"

signature_1_A = sign(message_1, keypair_A.private_key)
signature_1_B = sign(message_1, keypair_B.private_key)
signature_2_A = sign(message_2, keypair_A.private_key)
signature_2_B = sign(message_2, keypair_B.private_key)

println("Alice signature for message 1 ($(length(signature_1_A)) bytes): ", first(bytes2hex(signature_1_A), 16), "...")
println("Alice signature for message 2 ($(length(signature_2_A)) bytes): ", first(bytes2hex(signature_2_A), 16), "...")
println("Bob signature for message 1 ($(length(signature_1_B)) bytes): ", first(bytes2hex(signature_1_B), 16), "...")
println("Bob signature for message 2 ($(length(signature_2_B)) bytes): ", first(bytes2hex(signature_2_B), 16), "...")

println("\nSignature verification:")

println("\tAlice's public key:")

valid_AA1 = verify_sig(keypair_A.public_key, signature_1_A, message_1)
println("\t\tMessage 1, Alice's signature for 1: ", valid_AA1)
valid_AA2 = verify_sig(keypair_A.public_key, signature_2_A, message_1)
println("\t\tMessage 1, Alice's signature for  2: ", valid_AA2)
valid_AA3 = verify_sig(keypair_A.public_key, signature_1_A, message_2)
println("\t\tMessage 2, Alice's signature for  1: ", valid_AA3)
valid_AA4 = verify_sig(keypair_A.public_key, signature_2_A, message_2)
println("\t\tMessage 2, Alice's signature for  2: ", valid_AA4)

valid_AB1 = verify_sig(keypair_A.public_key, signature_1_B, message_1)
println("\t\tMessage 1, Bob's signature for 1: ", valid_AB1)
valid_AB2 = verify_sig(keypair_A.public_key, signature_2_B, message_1)
println("\t\tMessage 1, Bob's signature for  2: ", valid_AB2)
valid_AB3 = verify_sig(keypair_A.public_key, signature_1_B, message_2)
println("\t\tMessage 2, Bob's signature for  1: ", valid_AB3)
valid_AB4 = verify_sig(keypair_A.public_key, signature_2_B, message_2)
println("\t\tMessage 2, Bob's signature for  2: ", valid_AB4)

println("\tBob's public key:")

valid_BB1 = verify_sig(keypair_B.public_key, signature_1_B, message_1)
println("\t\tMessage 1, Bob's signature for 1: ", valid_BB1)
valid_BB2 = verify_sig(keypair_B.public_key, signature_2_B, message_1)
println("\t\tMessage 1, Bob's signature for 2: ", valid_BB2)
valid_BB3 = verify_sig(keypair_B.public_key, signature_1_B, message_2)
println("\t\tMessage 2, Bob's signature for 1: ", valid_BB3)
valid_BB4 = verify_sig(keypair_B.public_key, signature_2_B, message_2)
println("\t\tMessage 2, Bob's signature for 2: ", valid_BB4)

valid_BA1 = verify_sig(keypair_B.public_key, signature_1_A, message_1)
println("\t\tMessage 1, Alice's signature for 1: ", valid_BA1)
valid_BA2 = verify_sig(keypair_B.public_key, signature_2_A, message_1)
println("\t\tMessage 1, Alice's signature for 2: ", valid_BA2)
valid_BA3 = verify_sig(keypair_B.public_key, signature_1_A, message_2)
println("\t\tMessage 2, Alice's signature for 1: ", valid_BA3)
valid_BA4 = verify_sig(keypair_B.public_key, signature_2_A, message_2)
println("\t\tMessage 2, Alice's signature for 2: ", valid_BA3)
println()

hash_success = length(public_key_hash_A) == 32 && length(public_key_hash_B) == 32
sig_success_AA = valid_AA1 && !valid_AA2 && !valid_AA3 && valid_AA4
sig_success_AB = !valid_AB1 && !valid_AB2 && !valid_AB3 && !valid_AB4
sig_success_BA = !valid_BA1 && !valid_BA2 && !valid_BA3 && !valid_BA4
sig_success_BB = valid_BB1 && !valid_BB2 && !valid_BB3 && valid_BB4
success = hash_success && sig_success_AA && sig_success_AB && sig_success_BA && sig_success_BB

if success
    tprint(md"""
    !!! tip "Success"
        All cryptopgraphic primitive tests successful.
    """)
else
    tprint(md"""
    !!! danger "Failure"
        Some cryptopgraphic primitive tests failed.
    """)
end