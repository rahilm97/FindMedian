arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4]
arr3 = [2]
arr4 = [1, 9, 11, 18]
arr5 = [9, 2, 17]
arr6 = [1, 2, 399, 444, 5, 99999, 555, 8000]
def findMedian(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return ((arr[n // 2] + arr[n // 2 - 1]) / 2)
    else:
        return arr[n // 2]

print(findMedian(arr1))
print(findMedian(arr2))
print(findMedian(arr3))
print(findMedian(arr4))
print(findMedian(arr5))
print(findMedian(arr6))