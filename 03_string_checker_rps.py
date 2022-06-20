# taken from rps
def string_checker(question, error, valid_list):

    valid = False
    while not valid:

        # ask user for choice (.lower choice)
        response = input(question).lower()

        # iterates through lists
        # full item name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error message
        print(error)
        print()


# main routine
# define shape list
shape_list = ["square", "triangle", "circle", "rectangle", "xxx"]

# looped for testing
while True:
    # ask user for shape
    shape = string_checker("Which shape do you wany to calculate? ", "<error> please enter a valid shape.", shape_list)

    if shape == "xxx":
        break

    print("Chosen Shape: {}\n".format(shape))
