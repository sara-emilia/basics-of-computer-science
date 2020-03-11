def tulostaRekursiivisesti(n):
    print n
    n2 = n - 1
    if n2 >= 0:
      tulostaRekursiivisesti(n2)