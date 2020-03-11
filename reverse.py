def reverse(merkkijono):
    reverse = ""
    for i in range(len(merkkijono), 0, -1):
        reverse += merkkijono[i-1]
    print reverse