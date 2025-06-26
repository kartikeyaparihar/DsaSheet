def merge(array,low,mid,high):
    left=array[low:mid+1]
    right=array[mid+1:high+1]
    i=0
    j=0
    k=low

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            array[k]=left[i]
            i+=1
        else:
                array[k]=right[j]
                j+=1
        k+=1
    while i<len(left):
        array[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        array[k]=right[j]
        j+=1
        k+=1

def mergeSort(array,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    mergeSort(array,low,mid)
    mergeSort(array,mid+1,high)
    merge(array,low,mid,high)

array1=[4,3,5,7,8,2]
mergeSort(array1,0,len(array1)-1)
print("Sorted array",array1)    

        

