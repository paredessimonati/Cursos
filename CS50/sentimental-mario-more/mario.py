from cs50 import get_int

# draw mario pyramids
# prompt user for height of pyramid
h = get_int("Enter the size of the pyramid: ")

# if user inputs int <1 and > 8 re prompt
while ((h < 1) or (h > 8)):
    h = int(input("Values must be between 1 and 8: "))
# generate pyramids of height h
for i in range(h):
    for j in range(h-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("#", end="")
    print("  ", end="")
    for k in range(i+1):
        print("#", end="")
    print()

