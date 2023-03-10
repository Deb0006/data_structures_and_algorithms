def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        merge(left)
        merge(right)

def mergeSort(left, right):
        sortedArr = []

        while(len(left), len(right)):
            if left[0] <= right[0]:
                sortedArr.append(left.pop())
            else:
                sortedArr.append(right.pop())
        return sortedArr + left+ right
    
    
        # # Two iterators for traversing the two halves
        # i = 0
        # j = 0
        
        # # Iterator for the main list
        # k = 0
        
        # while i < len(left) and j < len(right):
        #     if left[i] <= right[j]:
        #         # The value from the left half has been used
        #         arr[k] = left[i]
        #         # Move the iterator forward
        #         i += 1
        #     else:
        #         arr[k] = right[j]
        #         j += 1
        #     # Move to the next slot
        #     k += 1

        # # For all the remaining values
        # while i < len(left):
        #     arr[k] = left[i]
        #     i += 1
        #     k += 1

        # while j < len(right):
        #     arr[k]=right[j]
        #     j += 1
        #     k += 1

