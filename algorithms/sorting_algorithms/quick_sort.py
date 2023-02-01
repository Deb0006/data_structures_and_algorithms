def quickSort(arr):
  if len(arr) <= 2:
    return arr
  pivot  = arr[-1]
  left = []
  right = []
  for num in arr[:-1]:
    if num < pivot:
      left.append(num)
    else: 
      right.append(num)
  
  return quickSort(left)+ [pivot]+ quickSort(right)