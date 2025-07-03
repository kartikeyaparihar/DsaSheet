def MoveallZerostotheendofthearray(array):
    j=0
    for i in range(n):
        if array[i]==0:
            j=i
            break
    for i in range(j+1,n):
        if array[i]!=0:
            array[j],array[i]=array[i],array[j]
        else:
            j+=1
    return array
array=[1,2,0,3,0,4,0,5]
n=len(array)
print(MoveallZerostotheendofthearray(array))