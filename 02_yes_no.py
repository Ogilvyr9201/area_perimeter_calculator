def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes or no")
            print()



# main routine
# asks user if they want snacks 
while 1 == 1:
    used_before = yes_no("Have you used this program before? ")
    print("Answer: {}".format(used_before))
    print()