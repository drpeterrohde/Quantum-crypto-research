using SpecialFunctions
using Plots; gr()
using LaTeXStrings
using PlotThemes

theme(:default)

function bits_permutations(elements::Float64)::Float64
    return loggamma(elements+1)/log(2)
end

elements = range(1.0,10^5,step=1)
bits = bits_permutations.(elements)
#xticks = range(0,100000,step=25000)
#yticks = ([0 1.5*10^6], ["0", "1.5"])

fig1 = plot(elements, bits,
    xaxis = (L"\mathrm{elements}\,\,(N)", [0 10000], font(12, "Arial")),
    yaxis = (L"\mathrm{bits}\,\,(n)", [0 1.5*10^5], font(12, "Arial")),
    legend = :none,
    framestyle = :box,
    lw = 2
)
xticks!([0, 25000, 50000, 75000, 100000], [L"0", L"0.25\times 10^5", L"0.5\times 10^5", L"0.75\times 10^5", L"10^5"])
yticks!([0, 5*10^5, 10^6, 1.5*10^6], [L"0", L"0.5\times 10^6", L"1.0\times 10^6", L"1.5\times 10^6"])

savefig(fig1, "./bits_permutations.pdf")
plot(fig1)
