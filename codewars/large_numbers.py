def last_digit_list(lst):

    if not lst:
        return 1
    result = 1
    for num in lst[::-1]:
        result = num ** (result if result < 4 else result % 4 + 4)
        print(result)
    return result % 10
    
list = [2, 2, 101, 2]
print(last_digit_list(list))


# def last_digit(n1, n2):
#     """return last digit of huge numbers raised to huge powers"""
#     if n1 == 0 and n2 == 0:
#         return 1
#     if n2 == 0:
#         return 1
#     res = n2 % 4
#     if res == 0:
#         res = 4
#     num = pow(n1, res)
#     return num % 10

# print(last_digit(2 ** 200, 2 ** 300))