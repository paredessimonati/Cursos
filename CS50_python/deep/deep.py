text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
text = text.lower()
if "42" in text or "forty two" in text or "forty-two" in text:
    print("Yes")
else:
    print("No")