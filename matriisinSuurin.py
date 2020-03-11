def matriisinSuurin(matriisi):
    max = -9999
    for i in range(len(matriisi)):
        for j in range(len(matriisi[i])):
            if matriisi[i][j] > max:
                max = matriisi[i][j]
    return max