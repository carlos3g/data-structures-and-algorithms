def firstDuplicate(array):
    Set = set()
    for e in array:
        if e in Set:
            return e
        else:
            Set.add(e)
    return -1
