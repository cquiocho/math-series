def fibonacci(n):
  if n <= 0:
    return 0

  if n == 1:
    return 1

  if n == 2:
    return 1

  else:
   return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
  if n == 0:
    return 2

  if n == 1:
    return 1

  if n == 2:
    return 3

  else:
   return lucas(n - 1) + lucas(n - 2)
