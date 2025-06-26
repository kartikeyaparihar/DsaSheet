def largestElement(array):
    largest=array[0]
    for num in array:
        if num>largest:
            largest=num
    return largest

array=[2,4,45,674,34,56,6]
print("largest element in the array is ",largestElement(array))



