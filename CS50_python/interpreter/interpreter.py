math = input("please gimme equations\n")
x, y, z = math.split(" ")
if y == "+":
    print(float(int(x) + int(z)))
if y == "-":
    print(float(int(x) - int(z)))
if y == "*":
    print(float(int(x) * int(z)))
if y == "/":
    print(float(int(x) / int(z)))
