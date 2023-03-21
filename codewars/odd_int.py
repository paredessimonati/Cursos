def find_it(seq):
    seq_set = set(seq)
    return [number for number in seq_set if seq.count(number) % 2][0]