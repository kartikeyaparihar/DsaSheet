#def rotateArrayByk(array,k):
    #n=len(array)
    #k%=n
    #temp=array[:k]
    #for i in range(n):
   #     array[i]=array[i+k]
  #  array[-k:]=temp
 #   return array




#array=[1,2,3,4,5,6,7]

#print(rotateArrayByk(array,3))

def rotatebykelements(array,d):
    d=d%n
    temp=array[0:3]
    for i in range(d,n):
        array[i-d]=array[i]
    for i in range(d,n):
        array[n-d]=temp[i-(n-d)]
    return array
array=[1,2,3,2,4,5,7,4]
n=len(array)
print(rotatebykelements(array,3))