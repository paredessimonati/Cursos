def main():
    word = input("Please enter message to Twittify! ")
    print(shorten(word))


def shorten(word):
    x = ""
    for v in word:
        if v in ("aeiouAEIOU"):
            continue
        x += v
    return x


if __name__ == "__main__":
    main()