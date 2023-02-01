import numpy as np

def isPowerofTwo(n):
  x = int(np.log2(n))
  if pow(2, x) == n:
    return True
  else:
    return False

print(isPowerofTwo(1))
print(isPowerofTwo(8))
print(isPowerofTwo(15))

def isPowerBitWise(n):
  if n<1:
    return True
  return (n & (n-1))==0

print(isPowerBitWise(15))
print(isPowerBitWise(4))
