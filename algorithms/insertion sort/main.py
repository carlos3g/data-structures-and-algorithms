def insertion(array: list) -> list: 
    for i in range(1, len(array)): 
        chave = array[i]
        j = i-1
        while (j >=0 and chave < array[j]) : 
                array[j+1] = array[j] 
                j -= 1
        array[j+1] = chave 
    return array