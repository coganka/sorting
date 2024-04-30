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


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
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


def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)
    return arr


def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

test = [5, 1, 0, 2, 8, 4, 6, 1]
print(insertion_sort(test))