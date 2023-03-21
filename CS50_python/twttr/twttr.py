twittify = input("Please enter message to Twittify! ")
for v in twittify:
    if v in ("aeiouAEIOU"):
        continue
    print(v, end="")
print("")