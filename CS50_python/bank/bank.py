text = input("Hello sir\n")
text = text.lower().strip()
if text.startswith("hello") == True:
    print("$0")
elif text.startswith("h") == True:
    print("$20")
else:
    print("$100")