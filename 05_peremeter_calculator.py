import math


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
    
    # if the shape is Square 
    if shape == "square":
        perimeter = lengths[0] * 4

    elif shape == "circle":
        perimeter = 2 * pi * lengths[0]

    elif shape == "rectangle":
        perimeter = 2 * (lengths[0] + lengths[1])

    elif shape == "triangle":
        perimeter = lengths[0] + lengths[1] + lengths[2]
    
    return perimeter
    


# **** Main Routine ****
# define pi
pi = math.pi


# define shape list
shape_list = ["square", "triangle", "circle", "rectangle"]
yes_no_list = ["yes", "no"]


# defines more then 0 error as i use this a lot
above_0_error = "<error> please enter an integer above 0" # add gold slide

# ask user for shape
shape = ""
while shape != "xxx":
    
    # ask user for shape
    shape = string_checker("Which shape do you wany to calculate? ", "<error> please enter a valid shape.", shape_list)

    # break loop if exit code entered 
    if shape == "xxx":
        break

    print("Chosen Shape: {}\n".format(shape))

    # get info for square
    if shape == "square":
        sq_side = num_check("How long is one side of the square? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [sq_side])
        print("The perimeter is {:.2f}\n".format(perimeter))
    
    # get info for circle
    elif shape == "circle":
        radius = num_check("What is the radius? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [radius])
        print("The perimeter is {:.2f}\n".format(perimeter))

    # get info for recatngle
    elif shape == "rectangle":
        rec_base = num_check("How long is the base? ", above_0_error, float, 0)
        rec_height = num_check("How long is the height? ", above_0_error, float, 0)
        perimeter = perimeter_calculator(shape, [rec_base, rec_height])
        print("The perimeter is {:.2f}\n".format(perimeter))

    # get info for trinagle
    elif shape == "triangle":

        # ask if they have 3 sides
        want_pereimeter = string_checker("Do you have 3 sides? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for them
        if want_pereimeter == "yes":
            tr_side1 = num_check("How long is the first side? ", above_0_error, float, 0)
            tr_side2 = num_check("How long is the second side? ", above_0_error, float, 0)
            tr_side3 = num_check("How long is the third side? ", above_0_error, float, 0)
            perimeter = perimeter_calculator(shape, [tr_side1, tr_side2, tr_side3])
            print("The perimeter is {:.2f}\n".format(perimeter))

        # ask if they have the base and height
        want_area = string_checker("Do you have base and height? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for it
        if want_area == "yes":
            tr_base = num_check("How long is the base? ", above_0_error, float, 0)
            tr_height = num_check("How long is the height? ", above_0_error, float, 0)


