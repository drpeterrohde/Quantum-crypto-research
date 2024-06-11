using SpecialFunctions
using Plots; gr()
using PlotThemes
using LaTeXStrings
using ColorSchemeTools
using Plots.PlotMeasures

theme(:default)

function delta(Nc::Float64, k::Float64)::Float64
        if Nc < k
                return 1.0
        else
                return exp(-sqrt(Nc-k)/sqrt(k))
        end
end

k = collect(range(1.0, 100.0, step=1.0))
Nc = collect(range(1.0, 1000.0, step=1.0))

d = log10.(delta.(Nc,k'))

fig1 = contour(k, Nc, d,
        xaxis = (L"k", font(12, "Computer Modern")),
        yaxis = (L"r_{\!\!f}\, N_{\!\!C}", font(12, "Computer Modern")),
        levels = [-1, -1.5, -2, -2.5, -3, -3.5],
        clabels = true,
        cbar = false,
        framestyle = :box,
        right_margin=10px
)

savefig(fig1, "./fountain.pdf")

plot(fig1)
