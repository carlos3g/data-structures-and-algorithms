def binary_search(array: list, target: int) -> [int, None]:
    min_ = 0
    max_ = len(array)-1
    while (min_ <= max_):
        guess = min_ + ((max_ - min_) // 2)
        if array[guess] == target:
            return guess
        elif array[guess] < target:
            min_ = guess + 1
        else:
            max_ = guess - 1
    return None
