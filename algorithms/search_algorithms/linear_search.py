def linearSearch(arr,n):
  for i, num in enumerate(arr):
    if num == n:
      return i
  return -1
    
#BigO = O(n)
