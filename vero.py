def vero(palkka):
    vero = 0
    if palkka <= 1000:
        vero = palkka*0.1
        print vero
    if (palkka > 1000) and (palkka <= 1500):
        vero = palkka*0.15
        print vero
    if (palkka > 1500) and (palkka <= 2000):
        vero = palkka*0.22
        print vero
    if (palkka > 2000) and (palkka <= 3000):
        vero = palkka*0.3
        print vero
    if palkka > 3000:
        vero = palkka*0.45
        print vero