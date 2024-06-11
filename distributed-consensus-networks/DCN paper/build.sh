#!/bin/bash
latexmk -pdf -synctex=1 -bibtex -interaction=nonstopmode -file-line-error

# mainfile="DCN"
#pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$mainfile.tex"
#bibtex "$mainfile"
#pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$mainfile.tex"
#pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$mainfile.tex"
#echo "LaTeX build completed."
