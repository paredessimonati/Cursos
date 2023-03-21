def max_sequence(arr):
    """Using Kadane's algorithm"""
    if not arr:
        return 0
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        if max_sum < current_sum:
            max_sum = current_sum
    return max_sum
