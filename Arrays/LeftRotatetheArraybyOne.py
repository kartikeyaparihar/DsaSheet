#def leftRotatetheArraybyOne(array):
    #array1=[0]*n
    
    #if n<=1:
     #   return array
    
    #for i in range(1,n):
     #   array1[i-1]=array[i]
    #array1[n-1]=array[0]
   # for i in range(n):
  #      print(array1[i],end=" ")
 #   print()
#array=[1,2,3,4,5]
#n=len(array)
#print(leftRotatetheArraybyOne(array))


def leftrotate(array):
    temp =array[0]
    for i in range(1,n):
        array[i-1]=array[i]
    array[n-1]=temp
    return array
array=[1,2,4,5,6]
n=len(array)
print(leftrotate(array))
