#Find the cartesian product
# example:
# A = [1,2]
# B = [3,4]
# AxB = [[1,3], [1,4], [2,3], [2,4]]
def cartesian_p(arr1, arr2):
    result= []
    for i in arr1:
        for j in arr2:
            result.append([i,j])
    return result

