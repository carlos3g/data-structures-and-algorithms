def first_duplicate(array: list) -> [int, None]:
    Set = set()
    for e in array:
        if e in Set:
            return e
        else:
            Set.add(e)
    return None
