using SpecialFunctions
# using PGFPlotsX
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

function strategy_matrix(dim::Int64,p::Float64)::Matrix{Int}
    x = range(1,dim,step=1)
    y = range(1,dim,step=1)
    threshold = p*dim
    z = strategy.(x,y',Int(threshold))
    return z
end

function random_matrix(dim::Int64,p::Float64)::Matrix{Int}
    x = range(1,dim,step=1)
    y = range(1,dim,step=1)
    z = randomise.(x,y',p)
    return z
end

function strategy(x::Int,y::Int,threshold::Int)::Int
    return x <= threshold ? 1 : 0
end

function randomise(x::Int,y::Int,p::Float64)::Int
    return rand()<=p ? 1 : 0
end

dim = 100
p=0.1
S0 = strategy_matrix(dim,p)
R0 = random_matrix(dim,p)
p=0.3
S1 = strategy_matrix(dim,p)
R1 = random_matrix(dim,p)
figS0 = heatmap(S0, title=L"S(r=0.1)", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
figR0 = heatmap(R0, title=L"\hat\pi\cdot S(r=0.1)", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
# figS1 = heatmap(S1, title=L"S(r=0.3)", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
# figR1 = heatmap(R1, title=L"\hat\pi\cdot S(r=0.3)", color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"))
rectangle(w, h, x, y) = Shape(x .+ [0,w,w,0], y .+ [0,0,h,h])

figS1 = heatmap(S1, color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"), dpi=1200)
plot!(rectangle(20,20,15,15), lw=2, linecolor = plot_color(:yellow, 0.75), fillcolor = plot_color(:yellow, 0))
figR1 = heatmap(R1, color=:bluesreds, legend=false, axis=([], false), aspect_ratio=:equal, framestyle=:box,titlefont = font(20,"Computer Modern"), dpi=1200)
plot!(rectangle(20,20,15,15), lw=2, linecolor = plot_color(:yellow, 0.75), fillcolor = plot_color(:yellow, 0))

# savefig(figS0, "./strategy_entropy_S_p01.pdf")
# savefig(figR0, "./strategy_entropy_R_p01.pdf")
savefig(figS1, "./strategy_entropy_S_p03.svg")
savefig(figR1, "./strategy_entropy_R_p03.svg")

# savefig(figS1, "./strategy_entropy_S_p03.tex")
# savefig(figR1, "./strategy_entropy_R_p03.tex")

# plot(figS0,figR0,figS1,figR1,grid=(2,2))
plot(figS1,figR1,grid=(2,1))
