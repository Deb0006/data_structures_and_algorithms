def insertion(arr):
  for i in range(1,len(arr)):
    numbertoinsert = arr[i]
    j = i - 1
    while (j>=0) and (arr[j]>numbertoinsert):
      arr[j+1] = arr[j]
      j = j - 1
    arr[j+1] = numbertoinsert
  return arr    