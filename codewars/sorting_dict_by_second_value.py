def order_weight(string):
    list = string.split()
    weight_dict = {}
    for i, number in enumerate(list):
        rolling_sum = 0
        for letter in number:
            rolling_sum += int(letter)
        weight_dict[i] = [number, rolling_sum]
    sorted_list = sorted(weight_dict.values(), key=lambda x:(x[1], x[0]))
    sorted_list = " ".join([x[0] for x in sorted_list])
    return sorted_list



print(order_weight(("2000 10003 1234000 44444444 9999 11 11 22 123")))