def comp(a, b):
    if a is None or b is None:
        return False
    if len(a) != len(b):
        return False
    for i, number in enumerate(sorted(a, key = abs)):
        if abs(number) * abs(number) != sorted(b)[i]:
            return False
    return True