def sort_array(source_array):
    odds = []
    odd_positions = []
    for i, number in enumerate(source_array):
        if number % 2 == 1:
            odds.append(number)
            odd_positions.append(i)
    
    for i, number in enumerate(sorted(odds)):
        source_array[odd_positions[i]] = number
    return source_array