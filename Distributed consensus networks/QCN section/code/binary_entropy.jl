using Plots; gr()
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

p = range(0.0,1.0,step=0.01)
H = binary_entropy.(p)

fig1 = plot(p, H,
    xaxis = (L"p", [0 1], font(12, "Arial")),
    yaxis = (L"H_2(p)", [0 1], font(12, "Arial")),
    legend = :none,
    framestyle = :box,
    lw = 2
)
xticks!([0, 0.5, 1], [L"0", L"0.5", L"1"])
yticks!([0, 0.5, 1], [L"0", L"0.5", L"1"])
savefig(fig1, "./binary_entropy.pdf")
plot(fig1)