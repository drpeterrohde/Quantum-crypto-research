using TikzPictures
using Colors

function tikz_code(n, Clist)
    code = ""
    radius = 0.4

    for x in 1:n
        for y in 1:n
            index = x + (y-1)*n

            if index ∈ Clist
                line_color = "red"
                fill_color = "red"
            else
                line_color = "gray"
                fill_color = "gray"
            end

            code *= """
            \\draw[draw=$line_color, fill=$fill_color, fill opacity=0.25] ($x, $y, 0) circle ($radius);
            """

            if index ∈ Clist
                code *= """
                \\draw[draw=red] ($x,$y,0) -- (3,3,2.5);
                """
            end
        end
    end

    code *= """
        \\draw[draw=red, fill=red, fill opacity=0.25] (3, 3, 2.5) circle ($radius);
        """

    return code
end

n = 5

code = tikz_code(n, [1, 9, 16, 20, 24])
println(code)
file_path = "single_random_subset_map.tex"
open(file_path, "w") do file
    write(file, code)
end

tp = TikzPicture(code, options="scale=0.5")
