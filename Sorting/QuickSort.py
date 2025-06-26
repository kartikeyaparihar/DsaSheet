def partition(array,low,high):
    pivot=array[low]
    i=low+1
    j=high
    while True:
        while i<=high and array[i]<=pivot:
            i+=1
        while j>=low and array[j]>pivot:
            j-=1
        if i>j:
            break
        array[i],array[j]=array[j],array[i]

    array[low],array[j]=array[j],array[low]
    return j

def quickSort(array,low,high):
    if low < high:
        partition_index = partition(array, low, high)
        quickSort(array, low, partition_index - 1)
        quickSort(array, partition_index + 1, high)
array=[2,5,6,4,3,1]
quickSort(array, 0, len(array) - 1)
print("sorted array",array)