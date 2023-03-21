import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")
    elif sys.argv[1][-1:] != "g":
        sys.exit("Not an image")

    # setting up the variables and sending them to functions
    image1 = open_file(sys.argv[1])
    image2 = open_file("shirt.png")
    after = imageops(image1, image2)

    # all done
    after.save(sys.argv[2])

    # isolating the try


def open_file(filename):
    try:
        image = Image.open(filename)
    except FileNotFoundError:
        sys.exit("File not found")
    return image

    # resizing and pasting over


def imageops(image1, image2):
    image1 = ImageOps.fit(image1, image2.size)
    image1.paste(image2, image2)
    return image1


if __name__ == "__main__":
    main()
