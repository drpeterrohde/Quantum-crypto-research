using SpecialFunctions
using Plots; gr()
using PlotThemes
using LaTeXStrings
using ColorSchemeTools

theme(:default)

function Rfail(N::Int64, k::Int64, eps::Float64)::Float64
        if k <= N
                this_r::Float64 = beta_inc_inv(k,N-k+1,eps)[1]
                return this_r
        else
                return 0
        end
end

title = L"\varepsilon=10^{-3}"
eps = 10^(-3)

# Figure 1
xstep = 2000
ystep = 200
N = collect(range(1, 10^4, step=1))
k = collect(range(1, 10^3, step=1))
r = collect(range(0.1, 0.9, step=0.2))
xticks = [1; collect(range(xstep, maximum(N), step=xstep))]
yticks = [1; collect(range(ystep, maximum(k), step=ystep))]

rfail = Rfail.(N, k', eps)

# plot_colors = cgrad([:orange, :red])
# clist = permutedims(collect(make_colorscheme(collect(cgrad(plot_colors)), length(r))))

fig1 = contour(N, k, rfail',
        xaxis = (L"|\mathcal{C}|", [1 maximum(N)], xticks, font(12, "Computer Modern")),
        yaxis = (L"k", [0 maximum(k)], yticks, font(12, "Computer Modern")),
        titlefont = font(12, "Computer Modern"),
        xlims=(1,maximum(N)),
        ylims=(1,maximum(k)),
        levels=r,
        cbar=false,
        clabels=true,
        framestyle=:box,
        title=title
)

savefig(fig1, "./DCNFS.pdf")
plot(fig1)
