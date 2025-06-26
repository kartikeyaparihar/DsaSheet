def insertionSort(array):
    n=len(array)
    for i in range(1,n):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key

    return array
array=[1,3,6,5,4,2]
print(insertionSort(array))

       

