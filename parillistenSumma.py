def parillistenSumma(taulu):
    summa = 0
    for i in range(0, len(taulu), 2):
        summa = summa + taulu[i]
    return summa