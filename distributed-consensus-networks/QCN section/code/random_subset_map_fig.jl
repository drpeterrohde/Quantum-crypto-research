using TikzPictures
using Colors

function tikz_code(n, line_colors, fill_colors)
    tikz_code = ""
    radius = 0.3 / n

    tikz_code *= """
        % Nodes
        """
    for i in 1:n
        for j in 1:n
            x = i / n
            y = j / n
            rand_index = rand(1:length(line_colors))
            line_color = line_colors[rand_index]
            fill_color = fill_colors[rand_index]

            tikz_code *= """
            \\draw[draw=$line_color, fill=$fill_color, fill opacity=0.25, tdplot_rotated_coords] ($x, $y, 0) circle ($radius);
            """
        end
    end

    tikz_code *= """
    % Consensus sets
    """
    for i in 1:n
            theta = 2.0*pi*i/n
            x = cos(theta)/2 + 1/2
            y = sin(theta)/2 + 1/2
            line_color = line_colors[i]
            fill_color = fill_colors[i]

            tikz_code *= """
            \\draw[draw=$line_color, fill=$fill_color, fill opacity=0.25, tdplot_rotated_coords] ($x, $y, 1) circle ($radius);
            """
    end

    return tikz_code
end

n = 5
line_colors = ["red", "teal", "blue", "cyan", "orange", "magenta"]
fill_colors = ["red", "green", "blue", "cyan", "orange", "magenta"]

code = tikz_code(n, line_colors, fill_colors)
println(code)
file_path = "random_subset_map.tex"
open(file_path, "w") do file
    write(file, code)
end

# tp = TikzPicture(code, options="scale=0.5")
