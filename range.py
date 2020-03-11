def range(n):
    lista = []
    i = 0
    luku = 0
    c = n
    while i < n:
        luku = n - (c-i)
        lista.append(luku)
        i = i + 1
    return lista