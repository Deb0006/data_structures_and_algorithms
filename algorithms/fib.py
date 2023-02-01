def fibonacci(n):
  if n==0:
    return 0
  elif n == 1:
    return 1
  
  fib = [0, 1]
  
  for i in range(2,n):
    num = fib[i-1] + fib[i-2]
    fib.append(num)
  return fib

print(fibonacci(7))

#BigO is O(n)