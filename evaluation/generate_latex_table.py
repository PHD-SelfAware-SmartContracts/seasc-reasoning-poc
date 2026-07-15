"""
==========================================================
Generate LaTeX Table

Reads evaluation/results.csv

Produces

evaluation/results_table.tex

==========================================================
"""

import csv
from pathlib import Path


CSV_FILE = Path("evaluation/results.csv")
TEX_FILE = Path("evaluation/results_table.tex")


rows = []

with open(CSV_FILE, newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        rows.append(row)


with open(TEX_FILE, "w") as tex:

    tex.write("\\begin{table}[t]\n")
    tex.write("\\centering\n")
    tex.write("\\caption{Reasoning Evaluation Results}\n")
    tex.write("\\label{tab:rq2results}\n")
    tex.write("\\begin{tabular}{lcccc}\n")
    tex.write("\\toprule\n")

    tex.write(
        "Scenario & Decision & Runtime (ms) & Depth & Explanation\\\\\n"
    )

    tex.write("\\midrule\n")

    for row in rows:

        tex.write(

            f"{row['Scenario']} & "
            f"{row['Decision']} & "
            f"{row['Runtime(ms)']} & "
            f"{row['ReasoningDepth']} & "
            f"{row['ExplanationComplete']}\\\\\n"

        )

    tex.write("\\bottomrule\n")
    tex.write("\\end{tabular}\n")
    tex.write("\\end{table}\n")


print()

print("LaTeX table written to")

print(TEX_FILE)
