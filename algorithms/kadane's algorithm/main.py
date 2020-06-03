def maximum_sum_subarray(array: list) -> int:
    max_sum = current_sum = array[0]
    for e in array[1:]:
        current_sum = max(current_sum + e, e)
        max_sum = max(current_sum, max_sum)
    return max_sum
