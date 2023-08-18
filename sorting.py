def bubbleSort(arr):
    for _ in arr:
        for i in range(len(arr) - 1):
            if (arr[i+1] < arr[i]):
                swap(i, i+1, arr)
            else: 
                continue
    return arr


def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i
        minChanged = False
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
                minChanged = True
        if minChanged:
            swap(i, minIdx, arr)
    return arr


def insertionSort(arr):
    for i in range(len(arr)):
        if arr[i] < arr[0]:
            arr.insert(0, arr.pop(i))
        else:
            for j in range(1,len(arr)):
                if arr[i] <= arr[j] and arr[i] >= arr[j-1]:
                    arr.insert(j, arr.pop(i))
    return arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    leftIdx, rightIdx = 0, 0
    res = []
    while leftIdx < len(left) and rightIdx < len(right):
        if (left[leftIdx] < right[rightIdx]):
            res.append(left[leftIdx])
            leftIdx += 1
        else:
            res.append(right[rightIdx])
            rightIdx += 1
    return res + left[leftIdx:] + right[rightIdx:]


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    quick(arr, 0, len(arr)-1)
    return arr

def quick(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if (arr[left] >= arr[pivot] and arr[right] <= arr[pivot]):
            swap(left, right, arr)
        if (arr[left] <= arr[pivot]):
            left += 1
        if (arr[right] >= arr[pivot]):
            right -= 1
    swap(pivot, right, arr)
    quick(arr, start, right-1)
    quick(arr, right+1, end)
    return


def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

test = [5, 1, 0, 2, 8, 4, 6, 1]
print(insertionSort(test))