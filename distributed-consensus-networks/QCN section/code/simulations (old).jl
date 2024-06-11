using SpecialFunctions
using Plots; gr()
using PlotThemes
using LaTeXStrings

theme(:default)

function Rmajority(N::Int64, eps::Float64)::Float64
    k::Int64 = ceil(N/2)-1
    r::Float64 = beta_inc_inv(k+1,N-k,eps)[1]
    return r
end

function Pmajority(N::Int64, r::Float64)::Float64
    k::Int64 = ceil(N/2)-1
    p::Float64 = beta_inc(k+1,N-k,r)[1]
    return p
end

function logPmajority(N::Int64, r::Float64)::Float64
    plog::Float64 = -log2(Pmajority(N,r))
    return plog
end

# GR & other backends
function contour_majority_plot(x, y, xticks, yticks, levels)
    z = logPmajority.(x', y)

    fig = contourf(x, y, z,
        xaxis = (L"N", [1 maximum(xticks)], xticks, font(12, "Arial")),
        yaxis = (L"r", [0 maximum(yticks)], yticks, font(12, "Arial")),
        xscale = :log10,
        clabels = false,
        cbar = false,
        levels = levels,
        title = L"P_M(N,r)=\varepsilon",
        color = cgrad(:heat, categorical = true),
        lw = 1
    )

    return fig
end

# levels = 20.0:10.0:90.0

# N = range(1, 10^4, step=1)
# r = range(0, 0.5, length=1001)
# xticks = [1 10^1 10^2 10^3 10^4]
# yticks = range(0, 0.5, step=0.1)
# fig1 = contour_majority_plot(N, r, xticks, yticks, levels)

# N = range(1, 10^2, step=1)
# r = range(0, 0.1, length=1001)
# xticks = [1 10^1 10^2]
# yticks = range(0, 0.1, step=0.02)
# fig2 = contour_majority_plot(N, r, xticks, yticks, levels)

# savefig(fig1, "./majority_prob.pdf")
# savefig(fig2, "./majority_prob_zoom.pdf")
# plot(fig1,fig2)

N = collect(range(1, 10^4, step=1))
xticks = [1 10^1 10^2 10^3 10^4]
yticks = range(0, 0.5, step=0.1)
lambda = 10:10:90; eps = 2.0.^(-collect(lambda))
legend = permutedims([L"\varepsilon=2^{-%$l}" for l in lambda])

r = [Rmajority.(N, eps) for eps in eps] 
fig1 = plot(N, r,
        xaxis = (L"N", [1 maximum(xticks)], xticks, font(12, "Arial")),
        yaxis = (L"r", [0 maximum(yticks)], yticks, font(12, "Arial")),
        ylims = (0, 0.5),
        xscale = :log10,
        title = L"P_M(N,r)=\varepsilon",
        label = legend,
        lw = 1,
        minorgrid = false,
        palette = palette(:thermal)
)

plot(fig1)