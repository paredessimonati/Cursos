from cs50 import get_string

answer = get_string("Please Greet Me! ")
answer = answer.lower().strip()

def value(answer):
    if answer.startswith ("hello"):
        return "0"
    elif answer.startswith ("h"):
        return "20"
    else:
        return "100"
print(f"${value(answer)}")


