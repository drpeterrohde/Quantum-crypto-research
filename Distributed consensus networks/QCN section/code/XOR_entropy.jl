using SpecialFunctions
using Plots; gr()
using Measures
using LaTeXStrings
using PlotThemes

theme(:default)

function binary_entropy(p::Float64)::Float64
    if p == 0 || p == 1
        return 0
    else
        return -p*log2(p)-(1-p)*log2(1-p)
    end
end

function binary_random(p::Float64)::Int
    return rand() <= p ? 1 : 0
end

function binary_matrix(p::Float64, dim::Int64)::Matrix{Int}
    P = p.*ones(Float64,(dim,dim))
    M = binary_random.(P)
    return M
end

function mask(S::Int64,X::Int64)::Int
    if S+X == 1
        return 1
    else
        return 0
    end
end

function strategy_matrix(dim::Int64)::Matrix{Int}
    x = range(1,dim,step=1)
    y = range(1,dim,step=1)
    z = strategy.(x,y',dim)
    return z
end

function strategy(x::Int,y::Int,threshold::Int)::Int
    return x+y <= threshold+1 ? 1 : 0
end

dim = 70
M0 = binary_matrix(0.0,dim)
M025 = binary_matrix(0.25,dim)
M05 = binary_matrix(0.5,dim)
S = strategy_matrix(dim)
X0 = mask.(M0,S)
X025 = mask.(M025,S)
X05 = mask.(M05,S)

figS = heatmap(S, title=L"S", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
figM0 = heatmap(M0, title=L"X(p=0)", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
figM025 = heatmap(M025, title=L"X(p=0.25)", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
figM05 = heatmap(M05, title=L"X(p=0.5)", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
figX0 = heatmap(X0, title=L"S\oplus X", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
figX025 = heatmap(X025, title=L"S\oplus X", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
figX05 = heatmap(X05, title=L"S\oplus X", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))

row0=plot(figM0,figS,figX0,layout=grid(1,3))
row025=plot(figM025,figS,figX025,layout=grid(1,3))
row05=plot(figM05,figS,figX05,layout=grid(1,3))

combined=plot(row0,row025,row05,layout=grid(3,1))
savefig(combined, "./strategy_entropy.pdf")

# savefig(figS, "./strategy_entropy_S.pdf")
# savefig(figM0, "./strategy_entropy_M0.pdf")
# savefig(figM025, "./strategy_entropy_M025.pdf")
# savefig(figM05, "./strategy_entropy_M05.pdf")
# savefig(figX0, "./strategy_entropy_X0.pdf")
# savefig(figX025, "./strategy_entropy_X025.pdf")
# savefig(figX05, "./strategy_entropy_X05.pdf")

plot(figS)