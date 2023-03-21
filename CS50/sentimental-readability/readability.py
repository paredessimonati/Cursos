from cs50 import get_string


def main():
    # get text from the user
    text = get_string("Text: ")

    # runs algorithm
    L = float(count_letters(text) / count_words(text) * 100)
    S = float(count_sentences(text) / count_words(text) * 100)
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # prints grade
    if index in range(1, 17):
        print(f"Grade {index}")
    elif index > 16:
        print("Grade 16+")
    else:
        print("Before Grade 1")


# count letters
def count_letters(x):
    count = 0
    for char in x:
        if char.isalpha():
            count += 1
    # print(f"{count}")
    return count


# count words (needs to start with 1)
def count_words(x):
    count = 1
    for char in x:
        if char.isspace():
            count += 1
    # print(f"{count}")
    return count


# count sentences
def count_sentences(x):
    count = 0
    for char in x:
        if char in ['.', '!', '?',]:
            count += 1
    # print(f"{count}")
    return count


if __name__ == "__main__":
    main()