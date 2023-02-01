def fibb(n):
  if n == 0:
    return n
  elif n == 1:
    return n
  return fibb(n-1)+fibb(n-2)

print(fibb(6))
print(fibb(5))
print(fibb(4))
print(fibb(3))
print(fibb(2))
print(fibb(1))
print(fibb(0))


#Recursion
#BigO = 2^n