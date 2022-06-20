def string_checker(question, error, options):
    
    while True:
        # asks user for input
        response = input(question).lower()

        # runs through lists and checks if response in lists
        for var_list in options:
            if response in var_list:

                # if response - to item in list set to inital item of that list
                response = var_list[0]
                return response
            
        print(error)
        print()



# main routine
# define shape list
shape_list = [
    ["square", "s"],
    ["triangle", "t"],
    ["circle", "c"],
    ["rectangle", "r"],
    ["xxx"]
]


while True:
    # ask user for shape
    shape = string_checker("Which shape do you wany to calculate? ", "<error> please enter a valid shape.", shape_list)

    if shape == "xxx":
        break

    print("Chosen Shape: {}\n".format(shape))
