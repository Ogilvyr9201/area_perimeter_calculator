# Functions go here


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, low):

    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            if response > low:
                return response
            else:
                print(error)
                print()
                continue

        except ValueError:
            print(error)
            print()


# main routine
# ask user for there age

while True:
    side_length = num_check("What is the side length? ", "<error> enter a length above 0", float, 0)
    print("Length of Side: {}".format(side_length))