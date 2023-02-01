def bubbleSort(arr):
  swapped = True
  while swapped:
    count = 0  
    for i in range(len(arr)-1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        count += 1
    if count == 0:
      swapped = False
  return arr

#BigO = O(n^2)