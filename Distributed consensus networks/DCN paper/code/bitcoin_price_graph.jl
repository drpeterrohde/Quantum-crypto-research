using CSV
using DataFrames
using Plots
using PlotThemes

theme(:default)

df = CSV.read("bitcoin-energy-consumpti.csv", DataFrame)

x_data = df[:, "DateTime"]
y_data = df[:, "Minimum TWh per Year"]

p = plot(x_data, y_data .- 1,
    xticks=false, yticks=false,
    lw=4,
    color=:paleturquoise,
    label=false,
    framestyle=:box,
    linewidth=3)
plot!(x_data, y_data,
    xticks=false, yticks=false,
    lw=4,
    color=:royalblue1,
    label=false,
    framestyle=:box,
    foreground_color_border=:steelblue2,
    linewidth=3,
    background_color_inside=:white)

display(p)
savefig(p, "bitcoin_energy_consumption.pdf")