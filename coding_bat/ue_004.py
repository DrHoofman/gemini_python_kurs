def diff21(n):

  n = int(input("Bitte geben Sie eine zahl ein: "))

  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
n = 0 # Example value
print(diff21(n))
