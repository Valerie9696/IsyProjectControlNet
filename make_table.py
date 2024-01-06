import latextable
from texttable import Texttable

categories = ["Generation", "Editing", "Completion", "Style Transfer", "Superresolution"]
header = ("filler", "Image", "Video", "Pointcloud", "Audio", "Text")
values = []
values.append(categories)
table_cell_interior = ['\\begin{tabular}[c]{@{}l@{}} \n unconditional \n conditioned on:\n \\end{tabular}']
for i in range(0, len(header)):
    fill = table_cell_interior*len(categories)
    fill[0] = header[i]
    values.append(fill)

table_1 = Texttable()
table_1.set_cols_align(["l"]*len(categories))
table_1.set_cols_valign(["t"]*len(categories))
table_1.add_rows(values)
print('-- Example 1: Basic --')
print('Texttable Output:')
print(table_1.draw())

table = latextable.draw_latex(table=table_1, caption="Overview", caption_above=True)
print(table)
