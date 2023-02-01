import math

def prime(n):
  if n<2:
    return False
  else:
    for i in range(2, int(math.sqrt(n)+1)):
      if n%i==0:
        return False
  return True
  
print(prime(1))
print(prime(4))
print(prime(5))