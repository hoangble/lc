def merge(Arr, start, mid, end):
    # NOTE: The following code was taken directly from
    # the module page for this past week

    # temporary arrays to copy the elements of subarray
    leftArray_size = (mid - start) + 1
    rightArray_size = end - mid

    leftArray = [0] * leftArray_size
    rightArray = [0] * rightArray_size

    for i in range(0, leftArray_size):
        leftArray[i] = Arr[start + i]

    for i in range(0, rightArray_size):
        rightArray[i] = Arr[mid + 1 + i]

    i = 0
    j = 0
    k = start

    while i < leftArray_size and j < rightArray_size:
        if leftArray[i] < rightArray[j]:
            # filling the original array with the smaller element
            Arr[k] = leftArray[i]
            i = i + 1
        else:
            # filling the original array with the smaller element
            Arr[k] = rightArray[j]
            j = j + 1
        k = k + 1

    # copying remaining elements if any
    while i < leftArray_size:
        Arr[k] = leftArray[i]
        k = k + 1
        i = i + 1

    while j < rightArray_size:
        Arr[k] = rightArray[j]
        k = k + 1
        j = j + 1


def mergeSort(Arr, start, end):
    if start < end:
        mid = (start + end) // 2
        armergeSort(Arr, start, mid)
        mergeSort(Arr, mid + 1, end)
        merge(Arr, start, mid, end)
        retirm


def kthElement(Arr1, Arr2, k):
    Arr1 += Arr2
    return mergeSort(Arr1, 0, len(Arr1) - 1)


def main():
    #    Arr1 = [5,9,10,47]
    #    Arr2 = [1,16,11,1000]
    #    k = 4
    Arr1 = [1, 5, 6, 7, 13, 30]
    Arr2 = [2, 10, 15]
    k = 8
    element = kthElement(Arr1, Arr2, k)
    print(element[k])


# if __name__ == "__main__":
#    main()
