text = input("Gimmi a string\n")
if ":)" or ":(" in text:
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
print(text)
