def minimi(lista):
    min = 9
    for i in range(len(lista)):
        if lista[i] <= min:
            min = lista[i]
    return min