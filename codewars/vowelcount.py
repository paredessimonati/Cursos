def get_count(sentence):
    counter = 0
    vowel_list = ["a", "e", "i", "o", "u"]
    for letter in sentence:
        if letter in vowel_list:
            counter += 1
    return counter