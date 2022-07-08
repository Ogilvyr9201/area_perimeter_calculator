import math
from traceback import print_tb
import pandas


# Functions go here
# Number checker to make sure user inputs correctly
def num_check(question):

    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response > 0:
                return response
            
            else:
                print("<error> please enter a number above 0")
                print()
                continue

        except ValueError:
            print("<error> please enter a number above 0")
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


# calculates the area and perimeter
def a_p_calculator(shape, lengths):
     
    # work put the area of a square
    if shape == "square":
        area = lengths[0] ** 2
        perimeter = lengths[0] * 4

    # work out area and perimeter of a circle
    elif shape == "circle":
        area = pi * (lengths[0] ** 2)
        perimeter = 2 * pi * lengths[0]

    # work out area of a rectangle
    elif shape == "rectangle":
        area = lengths[0] * lengths[1]
        perimeter = 2 * (lengths[0] + lengths[1])

    # work out area of a triangle
    elif shape == "triangle":

        # if they have base and height
        if len(lengths) == 2:
            area = (lengths[0] * lengths[1]) / 2
            perimeter = "n.a"

        # if the have three sides
        else:
            # halfs perimeter for herons formula
            p = (lengths[0] + lengths[1] + lengths[2]) / 2

            # using herons formula
            # try to figure out area
            try:
                area = math.sqrt(p * (p - lengths[0]) * (p - lengths[1]) * (p - lengths[2]))

            # if there is a math error because the triangle is impossible return nothing
            except ValueError:
                print("A triangle with these sides does not exist. ")
                return ""
            perimeter = lengths[0] + lengths[1] + lengths[2]

    # returns area and perimeter
    return [perimeter, area]
    

# get shape dimensions
def shape_dimensions(shape):

    # get info for square or circle or rectrangle
    if shape in ("square", "circle"):
        # Ask a certain question if shape is square
        if shape == "square":
            side1 = num_check("How long is one side of the square? ")
            side2 = side1

        # ask a certain question if the shape is circle
        else:
            side1 = num_check("What is the radius of the circle? ")
            side2 = "n.a"

        # define side3 as nothing
        side3 = "n.a"

        # calculate perimeter and area
        dimensions = a_p_calculator(shape, [side1])

    # get info for recatngle
    elif shape == "rectangle":
        side1 = num_check("How long is the base? ")
        side2 = num_check("How long is the height? ")
        side3 = "n.a"

        # calculate area and perimeter
        dimensions = a_p_calculator(shape, [side1, side2])
    

    # get info for trinagle
    elif shape == "triangle":

        # ask if they have 3 sides
        want_perimeter = string_checker("Do you have the values of all 3 sides? ", "<error> please enter yes or no.", yes_no_list)

        # if they do have three sides, ask for them
        if want_perimeter == "yes":
            side1 = num_check("How long is the first side? ")
            side2 = num_check("How long is the second side? ")
            side3 = num_check("How long is the third side? ")

            # calculate perimeter and area
            dimensions = a_p_calculator(shape, [side1, side2, side3])

            # if the triangle is impossible
            if dimensions == "":
                perimeter = "triangle"
                area = "impossible"

            else:
                perimeter = dimensions[0]
                area = dimensions[1]

            # return information so that it breaks out of the function
            return [side1, side2, side3, perimeter, area]

        # ask if they have the base and height
        want_area = string_checker("Do you have the values of the base and height? ", "<error> please enter yes or no.", yes_no_list)

        # if they do have the base and height, ask for it
        if want_area == "yes":
            side1 = num_check("How long is the base? ")
            side2 = num_check("How long is the height? ")
            side3 = "n.a"

            # calculate area
            dimensions = a_p_calculator(shape, [side1, side2])
        
        if want_area == "no" and want_perimeter == "no":
            print("cannot calculate area or perimeter with no information\n")
            side1 = "n.a"
            side2 = "n.a"
            side3 = "n.a"
            dimensions = ["n.a", "n.a"]

    # define the area nd perimeter seperatly
    perimeter = dimensions[0]
    area = dimensions[1]

    # return information
    return [side1, side2, side3, perimeter, area]


# makes sure name is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if not response:
            print(error)
        else:
            return response


# instructions
def instructions():
    print("""*** Intructions ***
    
    This is a calculator for area and perimeter for 4 basic shpaes
    that can be used to check the answers for school questions.
    
    Shapes that can be calculated
    - Square (s)
    - Cricle (c)
    - Rectangle (r)
    - Triangle (t)
    
    For tirangle it will ask you if you have all three sides, and 
    if you dont it will ask you if you have the base and height.
    
    Once you are finished you use the exit code 'xxx' and you
    choose to make a text file with a table of information 
    called 'what you choose'_apc.txt\n\n""")


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

# ask user if they want the instructions
see_instructions = string_checker("Would you like to see instructions? " ,"PLease put in yes or no (y / n)", yes_no_list)
print()

# print instructions
if see_instructions == "yes":
    instructions()

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

    # tell user perimeter and area
    if isinstance(dimensions[3], str) == True and isinstance(dimensions[4], str) == True:
        print("\nThe perimeter is not calculated")
        print("The area is not calculated\n")
    elif isinstance(dimensions[3], str) == True:
        print("\nThe perimeter is not calculated")
        print("The area is {:.2f} Units squared\n".format(dimensions[4]))
    else:
        print("\nThe perimeter is {:.2f} Units".format(dimensions[3]))
        print("The area is {:.2f}\n Units squared".format(dimensions[4]))

    # add the dimensions to a list
    chosen_shape_list.append(shape.capitalize())
    side1_list.append(dimensions[0])
    side2_list.append(dimensions[1])
    side3_list.append(dimensions[2])
    perimeter_list.append(dimensions[3])
    area_list.append(dimensions[4])

print()

# generates variable frames
summary_frame = pandas.DataFrame(summary_dictionary)

# set index to shape 
summary_frame = summary_frame.set_index("Shape")
summary_frame = summary_frame.round(2)

# ask if user wants to write to file
want_file = string_checker("Would you like a text file of your results? ", "Pease eneter yes or no (y / n)", yes_no_list)
print()
if want_file == "yes":
    
    # ask user for file  name to make file
    name = not_blank("What would you like to call the file? ", "<error> name cannot be blank.")
    print()

    # frames to text
    file_title = "{} - Area / Perimeter Calculator".format(name.capitalize())
    summary_title = "*** Data Table ***"
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

