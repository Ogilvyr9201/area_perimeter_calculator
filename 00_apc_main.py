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
    

# get shape dimentions
    print("Chosen Shape: {}\n".format(shape))

    # get info for square
    if shape == "square":
        sq_side = num_check("How long is one side of the square? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [sq_side])
        area = area_calculator(shape, [sq_side])
        print("The area is {:.2f}\n".format(area))
    
    # get info for circle
    elif shape == "circle":
        radius = num_check("What is the radius? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [radius])
        area = area_calculator(shape, [radius])
        print("The area is {:.2f}\n".format(area))

    # get info for recatngle
    elif shape == "rectangle":
        rec_base = num_check("How long is the base? ", above_0_error, float, 0)
        rec_height = num_check("How long is the height? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [rec_base, rec_height])
        area = area_calculator(shape, [rec_base, rec_height])
        print("The area is {:.2f}\n".format(area))

    # get info for trinagle
    elif shape == "triangle":

        # ask if they have 3 sides
        want_pereimeter = string_checker("Do you have the values of all 3 sides? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for them
        if want_pereimeter == "yes":
            tr_side1 = num_check("How long is the first side? ", above_0_error, float, 0)
            tr_side2 = num_check("How long is the second side? ", above_0_error, float, 0)
            tr_side3 = num_check("How long is the third side? ", above_0_error, float, 0)
            perimeter = perimeter_calculator(shape, [tr_side1, tr_side2, tr_side3])
            area = area_calculator(shape, [tr_side1, tr_side2, tr_side3])
            print("The area is {:.2f}\n".format(area))

        # ask if they have the base and height
        want_area = string_checker("Do you have the values of the base and height? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for it
        if want_area == "yes":
            tr_base = num_check("How long is the base? ", above_0_error, float, 0)
            tr_height = num_check("How long is the height? ", above_0_error, float, 0)
            area = area_calculator(shape, [tr_base, tr_height, ])
            print("The area is {:.2f}\n".format(area))

    print("Chosen Shape: {}\n".format(shape))

    # get info for square
    if shape == "square":
        sq_side = num_check("How long is one side of the square? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [sq_side])
        area = area_calculator(shape, [sq_side])
        print("The area is {:.2f}\n".format(area))
    
    # get info for circle
    elif shape == "circle":
        radius = num_check("What is the radius? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [radius])
        area = area_calculator(shape, [radius])
        print("The area is {:.2f}\n".format(area))

    # get info for recatngle
    elif shape == "rectangle":
        rec_base = num_check("How long is the base? ", above_0_error, float, 0)
        rec_height = num_check("How long is the height? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [rec_base, rec_height])
        area = area_calculator(shape, [rec_base, rec_height])
        print("The area is {:.2f}\n".format(area))

    # get info for trinagle
    elif shape == "triangle":

        # ask if they have 3 sides
        want_pereimeter = string_checker("Do you have the values of all 3 sides? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for them
        if want_pereimeter == "yes":
            tr_side1 = num_check("How long is the first side? ", above_0_error, float, 0)
            tr_side2 = num_check("How long is the second side? ", above_0_error, float, 0)
            tr_side3 = num_check("How long is the third side? ", above_0_error, float, 0)
            perimeter = perimeter_calculator(shape, [tr_side1, tr_side2, tr_side3])
            area = area_calculator(shape, [tr_side1, tr_side2, tr_side3])
            print("The area is {:.2f}\n".format(area))

        # ask if they have the base and height
        want_area = string_checker("Do you have the values of the base and height? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for it
        if want_area == "yes":
            tr_base = num_check("How long is the base? ", above_0_error, float, 0)
            tr_height = num_check("How long is the height? ", above_0_error, float, 0)
            area = area_calculator(shape, [tr_base, tr_height, ])
            print("The area is {:.2f}\n".format(area))

    print("Chosen Shape: {}\n".format(shape))

    # get info for square
    if shape == "square":
        sq_side = num_check("How long is one side of the square? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [sq_side])
        area = area_calculator(shape, [sq_side])
        print("The area is {:.2f}\n".format(area))
    
    # get info for circle
    elif shape == "circle":
        radius = num_check("What is the radius? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [radius])
        area = area_calculator(shape, [radius])
        print("The area is {:.2f}\n".format(area))

    # get info for recatngle
    elif shape == "rectangle":
        rec_base = num_check("How long is the base? ", above_0_error, float, 0)
        rec_height = num_check("How long is the height? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [rec_base, rec_height])
        area = area_calculator(shape, [rec_base, rec_height])
        print("The area is {:.2f}\n".format(area))

    # get info for trinagle
    elif shape == "triangle":

        # ask if they have 3 sides
        want_pereimeter = string_checker("Do you have the values of all 3 sides? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for them
        if want_pereimeter == "yes":
            tr_side1 = num_check("How long is the first side? ", above_0_error, float, 0)
            tr_side2 = num_check("How long is the second side? ", above_0_error, float, 0)
            tr_side3 = num_check("How long is the third side? ", above_0_error, float, 0)
            perimeter = perimeter_calculator(shape, [tr_side1, tr_side2, tr_side3])
            area = area_calculator(shape, [tr_side1, tr_side2, tr_side3])
            print("The area is {:.2f}\n".format(area))

        # ask if they have the base and height
        want_area = string_checker("Do you have the values of the base and height? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for it
        if want_area == "yes":
            tr_base = num_check("How long is the base? ", above_0_error, float, 0)
            tr_height = num_check("How long is the height? ", above_0_error, float, 0)
            area = area_calculator(shape, [tr_base, tr_height, ])
            print("The area is {:.2f}\n".format(area))


# get shape dimensions
def shape_dimensions(shape):

    # get info for square
    if shape == "square":
        sq_side = num_check("How long is one side of the square? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [sq_side])
        area = area_calculator(shape, [sq_side])
        print("The perimeter is {:.2f}\n".format(perimeter))
        print("The area is {:.2f}\n".format(area))
        return [sq_side, perimeter, area]
    
    # get info for circle
    elif shape == "circle":
        radius = num_check("What is the radius? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [radius])
        area = area_calculator(shape, [radius])
        print("The perimeter is {:.2f}\n".format(perimeter))
        print("The area is {:.2f}\n".format(area))
        return [radius, perimeter, area]

    # get info for recatngle
    elif shape == "rectangle":
        rec_base = num_check("How long is the base? ", above_0_error, float, 0)
        rec_height = num_check("How long is the height? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [rec_base, rec_height])
        area = area_calculator(shape, [rec_base, rec_height])
        print("The perimeter is {:.2f}\n".format(perimeter))
        print("The area is {:.2f}\n".format(area))
        return [rec_base, rec_height,  perimeter, area]

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
            print("The perimeter is {:.2f}\n".format(perimeter))
            print("The area is {:.2f}\n".format(area))
            return ["3 sides", tr_side1, tr_side2, tr_side3, perimeter, area]

        # ask if they have the base and height
        want_area = string_checker("Do you have the values of the base and height? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for it
        if want_area == "yes":
            tr_base = num_check("How long is the base? ", above_0_error, float, 0)
            tr_height = num_check("How long is the height? ", above_0_error, float, 0)
            area = area_calculator(shape, [tr_base, tr_height, ])
            print("The perimeter is {:.2f}\n".format(perimeter))
            print("The area is {:.2f}\n".format(area))
            return ["base and height", tr_base, tr_height, perimeter, area]


# **** Main Routine ****
# define pi
pi = math.pi

# summary lists
shape_list = []
perimeter_list = []
area_list = []

# square lists
sq_sides = []
sq_perimeters = []
sq_areas = []

# circle lists
cr_radiae = []
cr_perimeters = []
cr_areas = []

# rectangle lists
rec_bases = []
rec_heights = []
rec_perimeters = []
rec_areas = []

# triangle lists
tr_bases = []
tr_heights = []
tr_side1s = []
tr_side2s = []
tr_side3s = []
tr_perimeters = []
tr_areas = []

# summary dictionary
summary_dictionary = {
    "Shape": shape_list,
    "Perimeter": perimeter_list,
    "Area": area_list
}

# square dictionarys
square_dictionary = {
    "Side": sq_sides,
    "Perimeter": sq_perimeters,
    "Area": sq_areas
}

# cricle dictionary 
circle_dictionary = {
    "Radius": cr_radiae,
    "Perimeter": cr_perimeters,
    "Area": cr_areas
}

# rectangle dictionary
rectangle_dictionary = {
    "Base": rec_bases,
    "Height": rec_heights,
    "Perimeter": rec_perimeters,
    "Area": rec_areas
}

# triangle dictionary
triangle_dictionary = {
    "Base": tr_bases,
    "Height": tr_heights,
    "Side 1": tr_side1s,
    "Side 2": tr_side2s,
    "Side 3": tr_side3s,
    "Perimeter": tr_perimeters,
    "Areas": tr_areas
}

# define shape list
shape_list = ["square", "triangle", "circle", "rectangle", "xxx"]
yes_no_list = ["yes", "no"]


# defines more then 0 error as i use this a lot
above_0_error = "<error> please enter an integer above 0" # add gold slide

# ask user for shape
shape = ""
while shape != "xxx":
    
    # ask user for shape
    shape = string_checker("Which shape do you want to calculate? ", "<error> please enter a valid shape.", shape_list)

    # break loop if exit code entered 
    if shape == "xxx":
        break

    dimensions = shape_dimensions(shape)

    if shape == "square":
        sq_sides.append(dimensions[0])
        sq_perimeters.append(dimensions[1])
        sq_areas.append(dimensions[2])
        perimeter_list.append(dimensions[1])
        area_list.append(dimensions[2])


    elif shape == "circle":
        cr_radiae.append(dimensions[0])
        cr_perimeters.append(dimensions[1])
        cr_areas.append(dimensions[2])

    elif shape == "rectangle":
        rec_bases.append(dimensions[0])
        rec_heights.append(dimensions[1])
        rec_perimeters.append(dimensions[2])
        rec_areas.append(dimensions[3])

    else:
        if dimensions[0] == "3 sides":
            tr_side1s.append(dimensions[1])
            tr_side2s.append(dimensions[2])
            tr_side3s.append(dimensions[3])
        
        elif dimensions[0] == "base and height":
            tr_bases.append(dimensions[1])
            tr_heights.append(dimensions[2])

    shape_list.append(shape)


# generates variable frames
summary_frame = pandas.DataFrame(summary_dictionary)

# frames to text
summary_txt = pandas.DataFrame.to_string(summary_frame)

# print summarys
print(summary_frame)