text = input("Please insert filename\n")
text = text.lower().strip()
if text.endswith(".gif") == True:
    print("image/gif")
elif text.endswith(".jpg") == True:
    print("image/jpeg")
elif text.endswith(".jpeg") == True:
    print("image/jpeg")
elif text.endswith(".png") == True:
    print("image/png")
elif text.endswith(".pdf") == True:
    print("application/pdf")
elif text.endswith(".txt") == True:
    print("text/plain")
elif text.endswith(".zip") == True:
    print("application/zip")
else:
    print("application/octet-stream")