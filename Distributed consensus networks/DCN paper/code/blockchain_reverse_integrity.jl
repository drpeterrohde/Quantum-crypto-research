using SpecialFunctions
using Plots; gr()
using PlotThemes
using LaTeXStrings
using ColorSchemes
using ColorSchemeTools
using Measures

theme(:default)

lambda = 80:-0.1:1
eps = 10.0.^(-collect(lambda))

# eps = 0:0.01:1
n = [1 2 5 10 25]
eps_dash = eps .^ n

legend = [L"n=%$i" for i in n]

# eps = collect(0.01:0.01:1)
eps_dash_cont = eps #collect(0.01:0.01:1)
n_cont = log.(eps_dash_cont)./log.(eps')

xticks = [10^-1, 10^-10, 10^-20]
yticks = xticks

fig_cont = contourf(eps, eps_dash_cont, n_cont,
        xaxis = (L"\varepsilon", xticks, font(12, "Computer Modern")),
        yaxis = (L"\varepsilon'", yticks, font(12, "Computer Modern")),
        xlims = (10^-20, 10^-1),
        ylims = (10^-20, 10^-1),
        clabels = false,
        cbar = false,
        levels = collect(1:1:25),
        # cscale = :log10,
        xscale = :log10,
        yscale = :log10,
        xflip = true,
        yflip = true,
        c=:turbid,
        lw=0,
        framestyle = :box
)

labels = [L"n=1" L"n=2" L"n=5" L"n=10" L"n=25"]
plot_colors = cgrad([:orange, :brown])
clist = permutedims(collect(make_colorscheme(collect(cgrad(plot_colors)), length(n)))) 

plot!(eps, eps_dash,
        xaxis = (L"\varepsilon", xticks, font(12, "Computer Modern")),
        yaxis = (L"\varepsilon'", yticks, font(12, "Computer Modern")),
        xlims = (10^-20, 10^-1),
        ylims = (10^-20, 10^-1),
        xscale = :log10,
        yscale = :log10,
        xflip = true,
        yflip = true,
        lw = 1,
        lc = clist,
        labels = labels,
        legendposition = :bottomright,
        framestyle = :box,
        right_margin = 5pt
)

savefig(fig_cont, "./blockchain_security_tradeoff.pdf")
plot(fig_cont)