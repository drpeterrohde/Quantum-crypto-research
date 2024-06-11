using SpecialFunctions
using Plots; gr()
using PlotThemes
using LaTeXStrings
using ColorSchemeTools

theme(:default)

function Tmajority(N::Int64, eps::Float64)::Float64
        k = floor(N/2)+1
        r::Float64 = beta_inc_inv(k,N-k+1, eps)[1]
        t::Float64 = -log.(1-r)
        return t
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
yticks = collect(range(0, 1.0, step=0.2))
t = [Tmajority.(N, eps) for eps in eps]

fig1 = plot(N, t,
        xaxis = (L"N", [1 maximum(xticks)], xticks, font(12, "Computer Modern")),
        yaxis = (L"t/\tau_r", [0 maximum(yticks)], yticks, font(12, "Computer Modern")),
        ylims = (0, 0.8),
        xscale = :log10,
        # yscale = :log10,
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
yticks = collect(range(0, 0.1, step=0.02))
t = [Tmajority.(N, eps) for eps in eps]

fig2 = plot(N, t,
        xaxis = (L"N", [1 maximum(xticks)], xticks, font(12, "Computer Modern")),
        yaxis = (L"t/\tau_r", [0 maximum(yticks)], yticks, font(12, "Computer Modern")),
        ylims = (0, 0.08),
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

savefig(fig1, "./DObS_time.pdf")
savefig(fig2, "./DObS_time_zoom.pdf")
plot(fig1, fig2)

rO = collect(range(0, 0.5, step=0.01))
tmax = log.(2 .-2*rO) 
fig3 = plot(rO, tmax,
        xaxis = (L"r(0)", [0 0.5], [0 0.25 0.5], font(12, "Computer Modern")),
        yaxis = (L"t_\mathrm{max}/\tau_r", [0 1], [0 1], font(12, "Computer Modern")),
        ylims = (0, 1),
        # title = "",
        titlefont = font(12, "Computer Modern"),
        # label = legend,
        legend = :none,
        # legendfontsize = 10,
        lw = 1,
        # lc = clist,
        framestyle = :box
        )
savefig(fig3, "./DObS_max_time.pdf")

t = collect(range(0, 4, step=0.01))
r0 = [0 0.1 0.2 0.3 0.4 0.5]
legend = [L"r(0)=0" L"r(0)=0.1" L"r(0)=0.2" L"r(0)=0.3" L"r(0)=0.4" L"r(0)=0.5"]
r = map(x -> 1 .-(1-x).*exp.(-t), r0)
fig4 = plot(t, [r[1], r[2], r[3], r[4], r[5], r[6]],
        xaxis = (L"t/{\tau_r}", [0 0.5], [0 0.25 0.5], font(12, "Computer Modern")),
        yaxis = (L"r(t)", [0 1], [0 1], font(12, "Computer Modern")),
        ylims = (0, 1),
        # title = "",
        titlefont = font(12, "Computer Modern"),
        label = legend,
        # legend = legend,
        legendfontsize = 10,
        lw = 1,
        lc = clist,
        framestyle = :box
        )

savefig(fig4, "./DObS_r_time.pdf")

plot(fig3, fig4)
