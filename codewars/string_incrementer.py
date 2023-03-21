def increment_string(string):
    count = 0
    if string[-1:].isdigit():
        for i in range(len(string)):
            if string[-(1+i):].isdigit():
                count += 1
            else:
                break
        number = str(int(string[-count:]) + 1).zfill(count)
        string = string[:-count] + number
        return string
    if string[-1:].isalpha:
        return string + "1"


print(increment_string("fo99obar00009"))




