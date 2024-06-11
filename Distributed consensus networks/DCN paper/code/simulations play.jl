using SpecialFunctions
using Plots; gr()
using PlotThemes
using LaTeXStrings

theme(:default)

function Pmajority(N::Int64, p::Float64)::Float64
    k::Int64 = floor(N/2)
    val = beta_inc(N-k,k+1,1-p)[2]
    return val
end

function diffEps(N1,N2,r)
    diff = Pmajority(N1,r) - Pmajority(N2,r)^4
    return diff
end

function contour_diff(N1, N2, r)
    z = diffEps.(N1,N2',r)
   # z = replace(z,-Inf=>-100)

    fig = contour(N1, N2, z,
       # xaxis = (L"N1", [1 maximum(xticks)], xticks, :log, font(12, "Arial")),
       # yaxis = (L"N2", [0 maximum(yticks)], yticks, font(12, "Arial")),
        cbar = false,
        legend = false,
        levels = [0.0],
#        title = L"P_M(N,r)=\varepsilon",
        color = :turbo,
        lw = 1
    )
   
     return fig
end


N1 = range(1, 10^4, step=10)
N2 = range(1, 10^4, step=10)
r=0.3
fig1 = contour_diff(N1, N2, r)

plot(fig1)


# function contour_majority_plot(x, y, xticks, yticks, levels)
#     z = log10.(Pmajority.(x', y))
#     z = replace(z,-Inf=>-100)

#     fig = contour!(x, y, z,
#         xaxis = (L"N", [1 maximum(xticks)], xticks, :log, font(12, "Arial")),
#         yaxis = (L"r", [0 maximum(yticks)], yticks, font(12, "Arial")),
#         clabels = ["a", "b", "c", "d", "e"],
#         cbar = false,
#         levels = levels,
#         title = L"P_M(N,r)=\varepsilon",
#         color = :turbo,
#         lw = 1
#     )
   
#      return fig
# end