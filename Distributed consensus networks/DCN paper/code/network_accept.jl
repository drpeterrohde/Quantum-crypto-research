using TikzPictures
using Colors

function tikz_code(x, y, p)
    myRad = 0.3/x

    tikz_code = """
    \\tdplotsetmaincoords{70}{110}
    \\begin{tikzpicture}[scale=2.5,tdplot_main_coords]
    \\def\\vOff{4}
    \\def\\myRad{$myRad}
    \\def\\myLW{0.25}
    \\def\\myHeight{0.75}
    \\def\\lineOp{0.1}
    """

    tikz_code *= """
        % Nodes
        """
    honest_nodes = []
    dishonest_nodes = []
    for i in 1:x
        for j in 1:y
            k=i+(j-1)*x
            xcoord::Float64 = ((i-1)-(x-1)/2)/(x-1)
            ycoord::Float64 = ((j-1)-(y-1)/2)/(y-1)

            if rand() <= p
                push!(honest_nodes, k)
                tikz_code *= """
                \\draw[draw=blue, line width=\\myLW, fill=cyan!20] ($xcoord, $ycoord, 0) circle (\\myRad) coordinate(n$k);
                """
            else
                push!(dishonest_nodes, k)
                tikz_code *= """
                \\draw[draw=red, line width=\\myLW, fill=red!20] ($xcoord, $ycoord, 0) circle (\\myRad) coordinate(n$k);
                """
            end
        end
    end

    tikz_code *= """
    \\draw[draw=none] (0,0,\\myHeight) coordinate(n0);
    """

    for i in 1:(x*y)
        if i in honest_nodes
            tikz_code *= """
            \\draw[draw=blue,opacity=\\lineOp] (n$i) -- (n0);
            """
        end
    end

    tikz_code *= """
    \\draw[blue, fill=blue!50] (0,0,\\myHeight) circle (1.5*\\myRad) coordinate(n0);
    \\node[scale=0.6] at (0, 0, \\myHeight+0.1) {\$\\mathcal{X}_\\mathcal{N}\$};
    \\node[scale=0.6] at (0, 0.7, 0) {\$\\mathcal{X}_{i\\in\\mathcal{N}}\$};
    \\end{tikzpicture}
    """

    return tikz_code
end

x = 15
y = 15
p = 0.6

code = tikz_code(x,y,p)
# println(code)
file_path = "./network_accept.tex"
open(file_path, "w") do file
    write(file, code)
end

# tp = TikzPicture(code, options="scale=0.5")
