import math
import pandas


# Functions go here
# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, low):

    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            if response > low:
                return response
            elif response == low:
                return ""
            else:
                print(error)
                print()
                continue

        except ValueError:
            print(error)
            print()


# taken from rps
def string_checker(question, error, valid_list, exit_code = None):

    valid = False
    while not valid:

        # ask user for choice (.lower choice)
        response = input(question).lower()

        # checks if exit code is put in and if there is one
        if exit_code is not None:
            if response == exit_code:
                return "xxx"

        # iterates through lists
        # full item name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error message
        print(error)
        print()


# calculates the perimeter
def perimeter_calculator(shape, lengths):
    
    if shape == "square":
        perimeter = lengths[0] * 4

    elif shape == "circle":
        perimeter = 2 * pi * lengths[0]

    elif shape == "rectangle":
        perimeter = 2 * (lengths[0] + lengths[1])

    elif shape == "triangle":
        perimeter = lengths[0] + lengths[1] + lengths[2]
    
    return perimeter
    

# calculates the area
def area_calculator(shape, lengths):
     
    if shape == "square":
        area = lengths[0] ** 2

    elif shape == "circle":
        area = pi * (lengths[0] ** 2)

    elif shape == "rectangle":
        area = lengths[0] * lengths[1]

    elif shape == "triangle":
        if len(lengths) == 2:
            area = (lengths[0] * lengths[1]) / 2

        else:
            # halfs perimeter for herons formula
            p = (lengths[0] + lengths[1] + lengths[2]) / 2
            # using herons formula
            area = math.sqrt(p * (p - lengths[0]) * (p - lengths[1]) * (p - lengths[2]))

    return area
    

# get shape dimensions
def shape_dimensions(shape):

    # get info for square
    if shape == "square":
        sq_side = num_check("How long is one side of the square? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [sq_side])
        area = area_calculator(shape, [sq_side])
        print("\nThe perimeter is {:.2f}".format(perimeter))
        print("The area is {:.2f}\n".format(area))
        return [sq_side, "n.a", "n.a", perimeter, area]
    
    # get info for circle
    elif shape == "circle":
        radius = num_check("What is the radius? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [radius])
        area = area_calculator(shape, [radius])
        print("\nThe perimeter is {:.2f}".format(perimeter))
        print("The area is {:.2f}\n".format(area))
        return [radius, "n.a", "n.a", perimeter, area]

    # get info for recatngle
    elif shape == "rectangle":
        rec_base = num_check("How long is the base? ", above_0_error, float, 0)
        rec_height = num_check("How long is the height? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [rec_base, rec_height])
        area = area_calculator(shape, [rec_base, rec_height])
        print("\nThe perimeter is {:.2f}".format(perimeter))
        print("The area is {:.2f}\n".format(area))
        return [rec_base, "n.a", rec_height,  perimeter, area]

    # get info for trinagle
    elif shape == "triangle":

        # ask if they have 3 sides
        want_perimeter = string_checker("Do you have the values of all 3 sides? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for them
        if want_perimeter == "yes":
            tr_side1 = num_check("How long is the first side? ", above_0_error, float, 0)
            tr_side2 = num_check("How long is the second side? ", above_0_error, float, 0)
            tr_side3 = num_check("How long is the third side? ", above_0_error, float, 0)
            perimeter = perimeter_calculator(shape, [tr_side1, tr_side2, tr_side3])
            area = area_calculator(shape, [tr_side1, tr_side2, tr_side3])
            print("\nThe perimeter is {:.2f}".format(perimeter))
            print("The area is {:.2f}\n".format(area))
            return [tr_side1, tr_side2, tr_side3, perimeter, area]

        # ask if they have the base and height
        want_area = string_checker("Do you have the values of the base and height? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for it
        if want_area == "yes":
            tr_base = num_check("How long is the base? ", above_0_error, float, 0)
            tr_height = num_check("How long is the height? ", above_0_error, float, 0)
            area = area_calculator(shape, [tr_base, tr_height, ])
            print("\nThe area is {:.2f}\n".format(area))
            return [tr_base, tr_height, "n.a", "n.a", area]
        
        if want_area and want_perimeter == "no":
            print("cannot calculate area or perimeter with no information\n")
            return ["n.a", "n.a", "n.a", "dummy", "n.a"]


# makes sure name is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if not response:
            print(error)
        else:
            return response


# **** Main Routine ****

# define pi
pi = math.pi

# summary lists
chosen_shape_list = []
side1_list = []
side2_list = []
side3_list = []
perimeter_list = []
area_list = []

# summary dictionary
summary_dictionary = {
    "Shape": chosen_shape_list,
    "  Side 1": side1_list,
    "  Side 2": side2_list,
    "  Side 3": side3_list,
    "Perimeter": perimeter_list,
    "Area": area_list
}

# define shape list
shape_list = ["square", "triangle", "circle", "rectangle", "xxx"]
yes_no_list = ["yes", "no"]


# defines more then 0 error as i use this a lot
above_0_error = "<error> please enter an integer above 0" # add gold slide

# Title
print("*** Area / Perimeter Caclulator ***\n")

# ask user for there name to make file name later
name = not_blank("What is your name? ", "<error> name cannot be blank.")

# ask user for shape
shape = ""
while shape != "xxx":
    
    # ask user for shape
    shape = string_checker("Which shape do you want to calculate? ", "<error> please enter a valid 2D shape. (square, rectangle, triangle, circle)", shape_list)

    # break loop if exit code entered 
    if shape == "xxx":
        break

    # ask user for the dimensions of the shape
    dimensions = shape_dimensions(shape)

    # add the dimensions to a list
    chosen_shape_list.append(shape.capitalize())
    side1_list.append(dimensions[0])
    side2_list.append(dimensions[1])
    side3_list.append(dimensions[2])
    perimeter_list.append(dimensions[3])
    area_list.append(dimensions[4])

print()
# print("*** Stuff in dictionary ***")
# summary_items = summary_dictionary.items()
# print(summary_items)

# generates variable frames
summary_frame = pandas.DataFrame(summary_dictionary)

# set index to shape 
summary_frame = summary_frame.set_index("Shape")
summary_frame = summary_frame.round(2)

# frames to text
file_title = "{} - Area / Perimeter Calculator".format(name.capitalize())
summary_title = "*** Summary Frame ***"
summary_txt = pandas.DataFrame.to_string(summary_frame)

# open text file
file_name = "{}_apc.txt".format(name)
text_file = open(file_name, "w+")

# to write list
to_write = [file_title, summary_title, summary_txt]

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# close file
text_file.close()

# print summarys
print(summary_frame)

