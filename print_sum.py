def print_sum():
  negatiiviset = [-1, -2, -3, -6, -7]
  positiiviset = [6, 8, 2, 5, 7]

  summa = 0
  if abs(negatiiviset[4]) > positiiviset[4]:
      for i in negatiiviset:
        summa=summa+i
      print negatiiviset[4], "oli suurempi:", summa
  else:
      for i in positiiviset:
        summa=summa+i
      print positiiviset[4], "oli suurempi:", summa