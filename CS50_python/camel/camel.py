snakefy = input("PleaseWriteSomethingInCamelCase: ")

# making exeption for First_letter
print(snakefy[0], end="")

# looping through characters 1 and onward
for camel in snakefy[1 :]:

    # replacing upper case with _ and lower case
    if camel.isupper() == True:
        print("_", end="")
        camel = camel.lower()

    # printing each lower case letter as it is
    print(camel, end="")

    #printing a new line
print("")
