def seuraavaJaollinen(n):
  if n%17==0:
    return n
  else:
    return seuraavaJaollinen(n+1)