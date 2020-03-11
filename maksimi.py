def maksimi(lista):
    max = 0
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max