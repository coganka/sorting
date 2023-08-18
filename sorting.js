function bubbleSort(arr) {
    for (let _ of arr) {
        for (let j = 0; j < arr.length - 1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(j, j+1, arr);
            } else {
                continue;
            }
        }
    }
    return arr
}


function selectionSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let min = i;
        let minChanged = false;
        for (let j = i+1; j < arr.length; j++) {
            if (arr[j] < arr[min]) {
                min = j;
                minChanged = true;
            }
        }
        if (minChanged) {
            swap(min, i, arr);
        }
    }
    return arr;
}


function insertionSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < arr[0]) {
            arr.unshift(arr.splice(i, 1)[0]);
        } else {
            for (let j = 1; j < arr.length; j++) {
                if (arr[i] <= arr[j] && arr[i] >= arr[j-1]) {
                    arr.splice(j, 0, arr.splice(i, 1)[0]);
                }
            }
        }
    }
    return arr;
}


function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }
    let mid = arr.length / 2;
    let left = arr.slice(0,mid);
    let right = arr.slice(mid);
    return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
    let res = [];
    let leftIdx = 0;
    let rightIdx = 0;
    while (leftIdx < left.length && rightIdx < right.length) {
        if (left[leftIdx] < right[rightIdx]) {
            res.push(left[leftIdx]);
            leftIdx++;
        } else {
            res.push(right[rightIdx]);
            rightIdx++;
        }
    }
    return res.concat(left.slice(leftIdx)).concat(right.slice(rightIdx));
}


function quickSort(arr) {
    if (arr.length <= 1) return arr;
    quickHelper(arr, 0, arr.length-1);
    return arr;
}

function quickHelper(arr, start, end) {
    if (start >= end) return;
    let pivot = start;
    let left = start + 1;
    let right = end;
    
    while (left <= right) {
        if (arr[left] > arr[pivot] && arr[right] < arr[pivot]) {
            swap(left, right, arr);
        }
        if (arr[left] <= arr[pivot]) {
            left++;
        }
        if (arr[right] >= arr[pivot]) {
            right--;
        }
    }
    swap(pivot, right, arr);
    quickHelper(arr, start, right-1);
    quickHelper(arr, right+1, end);
    return 
}

function swap(i, j, arr) {
    let temp = arr[i];    
    arr[i] = arr[j];
    arr[j] = temp;
    return arr;
}


const test = [3, 1, 5, 2, 0, 7, 2, 10];
console.log(quickSort(test));