import pandas
# from pandas import option_context

# summary dictionary testing
summary_dictionary = {
    "Shape": ["Square", "Rectangle", "Circle"],
    "  Side 1": [5, 4, 5],
    "  Side 2": ["n.a", 6, "n.a"],
    "  Side 3": ["n.a", "n.a", "n.a"],
    "Perimeter": [20, 20, 31.4],
    "Area": [25, 24, 76]
}

# generates variable frames
summary_frame = pandas.DataFrame(summary_dictionary)

# set index to shape 
summary_frame = summary_frame.set_index("Shape")
summary_frame = summary_frame.round(2)

# summary_frame.style.set_properties(subset=['text'], **{'width': '300px'})

# with pandas.option_context('display.max_colwidth', 400):
#     pandas.options.display(summary_frame.head())

print(summary_frame)