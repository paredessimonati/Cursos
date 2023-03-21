text = (input("Please enter as many words as you like \n")).split()
for words in text[: -1]:
    print(words + "...", end="")
print(text[len(text) - 1])