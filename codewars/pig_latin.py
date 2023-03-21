def pig_it(text):

    latin = [word[1:] + word[0] + "ay" if word.isalpha() else word for word in text.split()]
    return " ".join(latin)


# Lo mismo pero mas leible
# def pig_it(text):
    # text = text.split()
    # for word in text.copy():
    #     for letter in word:
    #         if letter.isalpha():
    #             word += letter
    #             word = word.replace(letter, "", 1)
    #             word += "ay"
    #             text.pop(0)
    #             text.append(word)
    #             break
    # return " ".join(text)
