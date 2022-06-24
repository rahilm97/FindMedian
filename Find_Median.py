arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4]
arr3 = [2]
def findMedian(arr):
    n = len(arr)
    if n % 2 == 0:
        return ((arr[n // 2] + arr[n // 2 - 1]) / 2)
    else:
        return arr[n // 2]
print(findMedian(arr1))
print(findMedian(arr2))
print(findMedian(arr3))