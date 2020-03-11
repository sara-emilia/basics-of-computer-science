def negatiiviset(lista):
    count = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            count = count + 1
    return count