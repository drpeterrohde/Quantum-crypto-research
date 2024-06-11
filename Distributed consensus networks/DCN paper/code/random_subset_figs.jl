using TikzPictures
using Colors

function tikz_random_subsets(n, xoff, yoff, line_colors, fill_colors)
    tikz_code = ""

    for i in 1:n
        for j in 1:n
            x = i / n + xoff
            y = j / n + yoff
            radius = 0.4 / n
            rand_index = rand(1:length(line_colors))
            line_color = line_colors[rand_index]
            fill_color = fill_colors[rand_index]

            tikz_code *= """
            \\draw[draw=$line_color, fill=$fill_color, fill opacity=0.25] ($x, $y) circle ($radius);
            """
        end
    end

    return tikz_code
end

function create_tikz_array(m, n, line_colors, fill_colors)
    ratio = 1.0/m
    tikz_code = """
    \\begin{tikzpicture}
    """
    for i in 1:m
        for j in 1:m
            this_pic = tikz_random_subsets(n, 1.2*i, 1.2*j, line_colors, fill_colors)
            tikz_code *= this_pic
        end
    end
    tikz_code *= """
    \\end{tikzpicture}
    """
    return tikz_code
end

n = 6
m = 3
line_colors = ["red", "teal", "blue", "cyan", "orange", "magenta"]
fill_colors = ["red", "green", "blue", "cyan", "orange", "magenta"]

tikz_code = create_tikz_array(m, n, line_colors, fill_colors)
println(tikz_code)
file_path = "random_subsets.tex"
open(file_path, "w") do file
    write(file, tikz_code)
end

tp = TikzPicture(tikz_code, options="scale=0.5")
