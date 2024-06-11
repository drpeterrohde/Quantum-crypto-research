using SpecialFunctions
using Plots; gr()
using PlotThemes
using LaTeXStrings
using ColorSchemeTools
using Plots.PlotMeasures

theme(:default)

function Rk(N::Int64, k::Int64, eps::Float64)::Float64
        if k <= N
                r::Float64 = 1-beta_inc_inv(k,N-k+1,eps)[1]
                # r::Float64 = beta_inc_inv(N-k,k+1,eps)[1]
                return r
        else
                return 0
        end
end

# Universal parameters
k = [1 20 40 60 80 100]
legend = permutedims([L"k=%k" for k in k])
plot_colors = cgrad([:orange, :red])
clist = permutedims(collect(make_colorscheme(collect(cgrad(plot_colors)), length(k))))

# Figure 1
N = collect(range(1, 10^3, step=1))
eps = 10^-4
xticks = [1, 250, 500, 750, 1000]#[1; range(10, maximum(N), step=20)]
yticks = range(0, 1, step=0.2)

r = Rk.(N, k[1], eps)

fig1 = plot(N, r,
        xaxis = (L"n=|\mathcal{C}|", [1 maximum(xticks)], xticks, font(12, "Computer Modern")),
        yaxis = (L"r", [0 maximum(yticks)], yticks, font(12, "Computer Modern")),
        xlims = (1, maximum(xticks)),
        ylims = (0, 1),
        # xscale = :log10,
        label = L"k=1",
        titlefont = font(12, "Computer Modern"),
        title = L"\varepsilon=10^{-4}",
        legend = :bottomright,
        legendfontsize = 10,
        lw = 1,
        lc = clist[1],
        framestyle = :box,
        right_margin=20px
)

r = Rk.(N, k[2], eps)
plot!(N,r,label=L"k=20",lc = clist[2])

r = Rk.(N, k[3], eps)
plot!(N,r,label=L"k=40",lc = clist[3])

r = Rk.(N, k[4], eps)
plot!(N,r,label=L"k=60",lc = clist[4])

r = Rk.(N, k[5], eps)
plot!(N,r,label=L"k=80",lc = clist[5])

r = Rk.(N, k[6], eps)
plot!(N,r,label=L"k=100",lc = clist[6])

savefig(fig1, "./DCNFS.pdf")
plot(fig1)

