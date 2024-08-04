using LaTeXStrings
import Base: sort, isless, isequal, hash, string

@enum GeneratorType Identity=1 NonEntropic=2 Entropic=3

struct GroupGenerator
    name::String
    type::GeneratorType
end

const GroupElement = Vector{GroupGenerator}
const Group = Vector{GroupElement}

function IdentityElement()::GroupElement
    return [GroupGenerator("", Identity)]
end

function TrivialGroup()::Group
    return [IdentityElement()]
end

function isequal(a::GroupGenerator, b::GroupGenerator)
    return (a.name == b.name) && (a.type == b.type)
end

function isequal(a::GroupElement, b::GroupElement)
    return all(x -> x ∈ b, a) && all(x -> x ∈ a, b)
end

function isless(a::GroupGenerator, b::GroupGenerator)
    if a.type != b.type
        return a.type < b.type
    end
    return a.name < b.name
end

function isless(a::GroupElement, b::GroupElement)
    g = sort(unique(a))
    h = sort(unique(b))

    for i ∈ 1:min(length(g), length(h))
        if g[i] != h[i]
            return isless(g[i], h[i])
        end
    end
    return length(a) < length(b)
end

function hash(g::GroupGenerator, h::UInt)
    return hash([g.name, g.type, h])
end

function hash(g::GroupElement, h::UInt)
    return hash(vcat(sort(g), h))
end

function normal_form(g::GroupElement)::GroupElement
    g_filt::GroupElement = filter(x -> x.type != Identity, g)
    g_sort_unqiue::GroupElement = sort(unique(g_filt))
    if length(g_sort_unqiue) == 0
        return IdentityElement()
    end
    return g_sort_unqiue
end

function element_product(g::GroupElement, h::GroupElement)::GroupElement
    generators = vcat(g,h)
    prod::GroupElement = []
    
    for gen ∈ generators
        if count(x -> x.name == gen.name, generators) == 1
            push!(prod, gen)
        end
    end

    prod_no_id::GroupElement = filter(g -> g.type != Identity, prod)
    prod_sort::GroupElement = sort(prod_no_id, by=x -> x.name)

    if length(prod_sort) == 0
        return [GroupGenerator("", Identity)]
    else
        return prod_sort
    end
end

function simplify_group(G::Group)::Group
    G = map(g -> normal_form(g), G)
    G = vcat([IdentityElement()], G)
    G = unique(G)
    G = sort(G)
    return G
end

function group_from_elements(elements::Vector{GroupElement})
    G::Group = group_product(elements, elements)
    return simplify_group(G)
end

function group_from_generators(generators::Vector{GroupGenerator})
    elements::Vector{GroupElement} = map(g -> [g], generators)
    return group_from_elements(elements)
end

function group_product(G::Group, H::Group)
    GH::Group = simplify_group(G)
    H_simp::Group = simplify_group(H)

    for h ∈ H_simp
        new_elements = []
        for g ∈ GH
            gh::GroupElement = element_product(g, h)
            if gh != []
                push!(new_elements, gh)
            end
        end
        GH = vcat(GH, new_elements)
    end

    return simplify_group(GH)
end

function group_element_product(G::Group, h::GroupElement)::Group
    Gh::Group = map(g -> element_product(g, h), G)
    return Gh
end

function entropic_elements(G::Group)::Vector{GroupElement}
    return filter(g -> all(x -> x.type == Entropic, g), G)
end

function mixed_elements(G::Group)::Vector{GroupElement}
    return filter(g -> any(x -> x.type == Entropic, g) && any(x -> x.type == NonEntropic, g), G)
end

function non_entropic_elements(G::Group)::Vector{GroupElement}
    return filter(g -> all(x -> x.type == NonEntropic, g), G)
end

function entropic_subgroup(G::Group)::Group
    elements = entropic_elements(G)
    subgroup = group_from_elements(elements)
    return subgroup
end

function non_entropic_subgroup(G::Group)::Group
    elements = non_entropic_elements(G)
    subgroup = group_from_elements(elements)
    return subgroup
end

function group_details(G::Group; format::Bool = false)::String
    str = ""

    if format
        G_ent = entropic_elements(G)
        G_non_ent = non_entropic_elements(G)
        G_mixed = mixed_elements(G)
    
        str *= string("|G| = ", length(G), "\n")
        str *= string("G = \\quad ", G_non_ent, "\n")
        str *= string("\\qquad\\quad ", G_mixed, "\n")
        str *= string("\\qquad\\quad ", G_ent, "\n")

        # str *= string("|G| = ", length(G), "\n")
        # str *= string("G(nonent) = ", G_non_ent, "\n")
        # str *= string("|G(nonent)| = " , length(G_non_ent), "\n")
        # str *= string("G(mixed) = ", G_mixed, "\n")
        # str *= string("|G(mixed)| = ", length(G_mixed), "\n")
        # str *= string("G(ent) = ", G_ent, "\n")
        # str *= string("|G(ent)| = ", length(G_ent), "\n")
    else
        str *= string("|G| = ", length(G), "\n")
        str *= string("G = ", G, "\n")
    end

    return str
end

function elements_diff(G::Group, H::Group)::Group
    G_norm = simplify_group(G)
    H_norm = simplify_group(H)
    diff_elements = filter(x -> !(x ∈ H_norm), G_norm)
    return diff_elements
end

function group_diff(G::Group, H::Group)::Group
    return group_from_elements(elements_diff(G, H))
end

function Base.show(io::IO, obj::GroupGenerator)
    print(io, string(obj))
end

function Base.string(obj::GroupGenerator)::String
    if obj.type == Identity
        return ""
    elseif obj.type == Entropic
        return "X($(obj.name))"
    elseif obj.type == NonEntropic
        return "$(obj.name)"
    end
end

function Base.string(obj::GroupElement)::String
    return "[" * join(map(string, obj), ".") * "]"
end

function Base.show(io::IO, obj::GroupElement)
    print(io, string(obj))
end

function Base.string(obj::Group)::String
    # return "{ \n  " * join(map(string, obj), ", \n  ") * "\n}"
    return "{ " * join(map(string, obj), ", ") * " }"
end

function Base.show(io::IO, obj::Group)
    print(io, string(obj))
end

function to_latex(str::String)
    str = replace(str, "\n" => "\\newline ")
    # str = replace(str, "." => "\\cdot ")
    str = replace(str, "." => " ")
    str = replace(str, "{" => "\\{ ")
    str = replace(str, "}" => "\\} ")
    str = replace(str, "[" => "\\, ")
    str = replace(str, "]" => "\\, ")
    # str = replace(str, r"X\((.*?)\)" => s"\\mathcal{X}_{\1}")
    str = replace(str, r"X\((.*?)\)" => s"\\mathcal{X}\1")
    return latexstring(str)
end
;