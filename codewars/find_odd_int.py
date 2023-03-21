def find_it(seq):
    unique_numbers = set(seq)
    for number in unique_numbers:
        if seq.count(number) % 2 == 1:
            return number
    return None