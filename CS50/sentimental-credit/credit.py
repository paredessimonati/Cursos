from cs50 import get_string
import sys

card = get_string("Please insert your credit card number: ")
digit = len(card)
if digit not in [13, 15, 16]:
    print("INVALID")
    sys.exit(1)
card_number = int(card)


# luhn's algorithm
sum1 = 0
for i in range(digit-2, -1, -2):
    double = int(card[i]) * 2
    for sub_digit in str(double):
        sum1 += int(sub_digit)
    sum1 += int(card[i + 1])

# cant make the card[i] get to 0.. so if the number is 13 or 15 im
# doing that... maybe ive been coding too long today and cant see
# a simple answer
if digit in (13, 15):
    sum1 += int(card[0])


# checking for last digit of sum1, if its 0, then the algorithm is true
last = str(sum1)
last_digit = int(last[len(last)-1])

if (last_digit != 0):
    print(f"{last_digit}")
    print("INVALID")
    sys.exit(1)

# Verifying card company
first_two = int(card[0] + card[1])
if first_two in range(51, 56):
    print("MASTERCARD")
if first_two in (34, 37):
    print("AMEX")
if first_two in range(40, 50):
    print("VISA")
else:
    print("INVALID")
