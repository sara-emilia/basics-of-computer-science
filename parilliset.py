def parilliset(n, m):
  while n <= m:
    if n%2 == 0:
      print n
    parilliset(n+1, m)
    return