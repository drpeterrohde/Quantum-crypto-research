using SpecialFunctions
using Plots; gr()
using PlotThemes
using LaTeXStrings
using ColorSchemeTools

theme(:default)

function Rmajority(N::Int64, eps::Float64)::Float64
        k = floor(N/2)+1
        r::Float64 = beta_inc_inv(k,N-k+1, eps)[1]
        return r
end

# Universal parameters
lambda = 10:10:80
eps = 2.0.^(-collect(lambda))
legend = permutedims([L"\varepsilon=2^{-%$l}" for l in lambda])
plot_colors = cgrad([:orange, :orangered2])
clist = permutedims(collect(make_colorscheme(collect(cgrad(plot_colors)), length(lambda)))) #reshape(range(colorant"red", stop=colorant"blue",length=length(lambda)), 1, length(lambda))#[cgrad(:inferno)[i] for i in range(0,1,length=length(lambda))]
title = L"P_{\!\!c}(N,r)=\varepsilon"

# Figure 1
N = collect(range(1, 10^4, step=1))
xticks = [1 10^1 10^2 10^3 10^4]
yticks = range(0, 0.5, step=0.1)
r = [Rmajority.(N, eps) for eps in eps]

fig1 = plot(N, r,
        xaxis = (L"N", [1 maximum(xticks)], xticks, font(12, "Computer Modern")),
        yaxis = (L"r", [0 maximum(yticks)], yticks, font(12, "Computer Modern")),
        ylims = (0, 0.5),
        xscale = :log10,
        title = title,
        titlefont = font(12, "Computer Modern"),
        label = legend,
        legend = :topleft,
        legendfontsize = 10,
        lw = 1,
        lc = clist,
        framestyle = :box
)

# Figure 2
N = collect(range(1, 10^2, step=1))
xticks = [1 10^1 10^2]
yticks = range(0, 0.1, step=0.02)
r = [Rmajority.(N, eps) for eps in eps]

fig2 = plot(N, r,
        xaxis = (L"N", [1 maximum(xticks)], xticks, font(12, "Computer Modern")),
        yaxis = (L"r", [0 maximum(yticks)], yticks, font(12, "Computer Modern")),
        ylims = (0, 0.1),
        xscale = :log10,
        title = title,
        titlefont = font(12, "Computer Modern"),
        label = legend,
        legend = :topleft,
        legendfontsize = 10,
        lw = 1,
        lc = clist,
        framestyle = :box
)

# Figure 3
N = collect(range(1, 10^4, step=1))
xticks = [1 10^1 10^2]
yticks = range(0, 0.5, step=0.1)
p = [1.0 0.9 0.8 0.7 0.6 0.5]
r = Rmajority.(N, 2^(-30)) .* p
legend = [L"p={%$p}" for p in p]
title = L"P_{\!\!c}(N,r)=\varepsilon"
plot_colors = cgrad([:blue, :deepskyblue])
clist = permutedims(collect(make_colorscheme(collect(cgrad(plot_colors)), length(p))))

fig3 = plot(N, r,
        xaxis = (L"N", [1 maximum(xticks)], xticks, font(12, "Computer Modern")),
        yaxis = (L"r", [0 maximum(yticks)], yticks, font(12, "Computer Modern")),
        ylims = (0, 0.5),
        xscale = :log10,
        title = title,
        titlefont = font(12, "Computer Modern"),
        label = legend,
        legend = :topleft,
        legendfontsize = 10,
        lw = 1,
        lc = clist,
        legendtitle = L"(\varepsilon=2^{-30})",
        legendtitlefontsize = 9,
        framestyle = :box
)

# Figure 4
# N = collect(range(1, 10^4, step=1))
xticks = range(0.5, 1, step=0.1)
yticks = range(0, 0.5, step=0.1)
N = [1 10 10^2 10^3 10^4]
p = range(0.5, 1, step=0.01)
r = Rmajority.(N, 2^(-30)) .* p
legend = [L"N=10^{%$n}" for n in [0 1 2 3 4]]
title = L"P_{\!\!c}(N,r)=\varepsilon"
plot_colors = cgrad([:blue, :deepskyblue])
clist = permutedims(collect(make_colorscheme(collect(cgrad(plot_colors)), length(N))))

fig4 = plot(p, r,
        xaxis = (L"p", [minimum(xticks) maximum(xticks)], xticks, font(12, "Computer Modern")),
        yaxis = (L"r", [0 maximum(yticks)], yticks, font(12, "Computer Modern")),
        ylims = (0, 0.5),
        # xscale = :log10,
        title = title,
        titlefont = font(12, "Computer Modern"),
        label = legend,
        legend = :topleft,
        legendfontsize = 10,
        lw = 1,
        lc = clist,
        legendtitle = L"(\varepsilon=2^{-30})",
        legendtitlefontsize = 9,
        framestyle = :box
)

savefig(fig1, "./majority_prob.pdf")
savefig(fig2, "./majority_prob_zoom.pdf")
savefig(fig3, "./majority_prob_p.pdf")
savefig(fig4, "./majority_prob_N.pdf")
plot(fig1, fig2)
plot(fig3)
plot(fig4)
