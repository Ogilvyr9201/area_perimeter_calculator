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



# **** Main Routine ****
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
        print("Side length is {}\n".format(sq_side))
    
    # get info for circle
    elif shape == "circle":
        radius = num_check("What is the radius? ", above_0_error, float, 0)
        print("Radius length is {}\n".format(radius))

    # get info for recatngle
    elif shape == "rectangle":
        rec_base = num_check("How long is the base? ", above_0_error, float, 0)
        rec_height = num_check("How long is the height? ", above_0_error, float, 0)
        print("Base length is {}".format(rec_base))
        print("Height length is {}\n".format(rec_height))

    # get info for trinagle
    elif shape == "triangle":

        # ask if they have 3 sides
        peremeter = string_checker("Do you have 3 sides? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for them
        if peremeter == "yes":
            tr_side1 = num_check("How long is the first side? ", above_0_error, float, 0)
            tr_side2 = num_check("How long is the second side? ", above_0_error, float, 0)
            tr_side3 = num_check("How long is the third side? ", above_0_error, float, 0)
            print("Side 1 length is {}".format(tr_side1))
            print("Side 2 length is {}".format(tr_side2))
            print("Side 3 length is {}\n".format(tr_side3))

        # ask if they have the base and height
        area = string_checker("Do you have base and height? ", "<error> please enter yes or no.", yes_no_list)

        # if they do ask for it
        if area == "yes":
            tr_base = num_check("How long is the base? ", above_0_error, float, 0)
            tr_height = num_check("How long is the height? ", above_0_error, float, 0)
            print("Base length is {}".format(tr_base))
            print("Height length is {}\n".format(tr_height))