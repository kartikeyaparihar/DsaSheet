def RecursiveBubbleSort(array,n):
    if n==1:
        return
    for i in range(n-1):
        if array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]

    RecursiveBubbleSort(array,n-1)
array=[1,3,4,5,2,6]
RecursiveBubbleSort(array,len(array))
print("sorted array",array)