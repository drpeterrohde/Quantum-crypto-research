using TikzPictures
using Colors

function tikz_code(n, x, y, r)
    tikz_code = """
    \\tdplotsetmaincoords{70}{110}
    \\begin{tikzpicture}[scale=0.5,tdplot_main_coords]
    \\def\\vOff{4}
    """

    tikz_code *= """
        % Nodes
        """
    for i in 1:x
        for j in 1:y
            k=i+(j-1)*x
            xcoord = i-1-x/2
            ycoord = j-1-y/2
            tikz_code *= """
            \\draw[draw=red, fill=red, fill opacity=0.25] ($xcoord, $ycoord, 0) circle (0.2) coordinate(n$k);
            """
        end
    end

    tikz_code *= """
    % Consensus sets (dummies)
    """
    for i in 1:n
            theta = 2.0*pi*i/n
            xcoord = r*cos(theta)/2
            ycoord = r*sin(theta)/2

            tikz_code *= """
            \\draw[draw=none] ($xcoord, $ycoord, \\vOff) circle (0.2) coordinate(c$i);
            """
    end

    for i in 1:(x*y)
        j=rand(1:n)
        tikz_code *= """
        \\draw[draw=red,opacity=0.15] (n$i) -- (c$j);
        """
    end

    for i in 1:n
        for j in 1:n
            tikz_code *= """
            \\draw[draw=cyan, opacity=0.5, line width=0.5] (c$i) -- (c$j);
            """
        end
    end

    for i in 1:n
            theta = 2.0*pi*i/n
            xcoord = r*cos(theta)/2
            ycoord = r*sin(theta)/2

            tikz_code *= """
            \\draw[draw=blue, fill=cyan!20] ($xcoord, $ycoord, \\vOff) circle (0.2);
            """
    end

    tikz_code *= """
    \\end{tikzpicture}
    """

    return tikz_code
end

n = 7
x = 7
y = 7
r = 4
# line_colors = ["red", "teal", "blue", "cyan", "orange", "magenta"]
# fill_colors = ["red", "green", "blue", "cyan", "orange", "magenta"]

code = tikz_code(n,x,y,r)
# println(code)
file_path = "market_network.tex"
open(file_path, "w") do file
    write(file, code)
end

;
# tp = TikzPicture(code, options="scale=0.5")
