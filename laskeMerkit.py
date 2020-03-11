def laskeMerkit(merkkijono):
    count = 0
    for i in range(len(merkkijono)):
        if merkkijono[i] == "e" or merkkijono[i] == "a":
            count = count + 1
    print count