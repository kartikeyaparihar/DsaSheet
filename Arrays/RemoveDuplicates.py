def duplicates(array):
        i=0
        for j in range(1,len(array)):
            if array[i]!=array[j]:
                i+=1
                array[i]=array[j]
        return i+1
array=[1,2,3,5,5]
k=duplicates(array)
print("Elements after removing the duplicates is ")
for i in range(k):
     print(array[i],end=" ")
