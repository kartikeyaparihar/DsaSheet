def recursiveInsertionSort(array,i,n):
    if i==n:
            return
    j=i
    for j in range(0,n):
        while j>0 and array[j-1]>array[j]:
            array[j-1],array[j]=array[j],array[j-1]
            j-=1
    recursiveInsertionSort(array,i+1,n)
array=[1,4,6,3,5,2]
n=len(array)
recursiveInsertionSort(array,0,n)
print("sorted array",array)

                  