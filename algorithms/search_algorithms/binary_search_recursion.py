def binarySearchRec(arr, n):
  return search(arr, n, 0, len(arr)-1)

def search(arr, n, left, right):
  if left>right:
    return -1
  mid = int((right + left)/2)
  
  if arr[mid] == n:
    return mid
  if arr[mid] > n:
    return search(arr, n, left, mid - 1)
  elif arr[mid] < n:
    return search(arr, n, mid + 1, right)
    

#BigO =  O(logn)