from cs50 import get_string

def main():
    text = get_string("Text: ")

    L = float(count_letters(text) / count_words(text) * 100)
    S = float(count_sentences(text)) / count_words(text) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if 1 <= index < 17:
        print(f"Grade {index}")
    elif index >= 17:
        print("Grade 16+")
    else:
        print("Before Grade 1")

def count_letters(text):
    return sum(char.isalpha() for char in text)

def count_words(text):
    return len(text.split())

def count_sentences(text):
    return sum(char in '.!?' for char in text)

if __name__ == "__main__":
    main()
