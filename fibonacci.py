def fibonacci(x):
  count = 0
  numb = 1
  while count < x:
    numb = numb + count
    count = count + numb
    if numb <= x:
        print numb
    if count <= x:
      print count