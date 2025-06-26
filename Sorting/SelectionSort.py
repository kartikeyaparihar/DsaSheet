def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i
        # Find the actual minimum element in the unsorted part
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first element of unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr1 = [13, 46, 24, 52, 20, 9]
print(selection_sort(arr1))  # Output: [9, 13, 20, 24, 46, 52]
