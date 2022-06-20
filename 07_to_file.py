import pandas
# information that will be written to file

# shape_list = []
# perimeter_list = []
# area_list = []

summary_dictionary = {
    "Shape": ["square", "rectangle", "triangle"],
    "Perimeter": [20, 20, 12],
    "Area": [25, 24, 6]
}

rectangle_dictionary = {
    "Side": [4, 5, 6, 7],
    "Perimeter": [16, 20, 24, 28],
    "Area": [16, 25, 36, 49]
}

user_name = "Ryan"
summary_title = "**** Summary Data ****"
shape_title = "--- Rectangle Data ---"

# generates variable frames
summary_frame = pandas.DataFrame(summary_dictionary)
rectangle_frame = pandas.DataFrame(rectangle_dictionary)

# frames to tewt
summary_txt = pandas.DataFrame.to_string(summary_frame)
rectangle_txt = pandas.DataFrame.to_string(rectangle_frame)

# print summarys
print(summary_frame)

# write to file...
#create file hold data (add .txt extention)
file_name = "{}_apc.txt".format(user_name)
title = "{} - Area / Perimeter Calculator".format(user_name)
text_file = open(file_name, "w+")

# to write list
to_write = [title, summary_title, summary_txt, shape_title, rectangle_txt]

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")
