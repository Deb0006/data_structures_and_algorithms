def binarySearch(arr, n):
  left = 0
  right = len(arr)-1
  
  while left <= right:
    mid = int((right + left)/2)
    if arr[mid] == n:
      return mid
    if arr[mid] > n:
      right = mid - 1
    elif arr[mid] < n:
      left = mid + 1
    
  return -1

#bigO = O(logn)

