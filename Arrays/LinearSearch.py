def LinearSearch(array):
    for i in range(n):
        if array[i] == target:
            return i
        else:
            print("The number is not present in the array")
        
    return -1
        
array=[1,2,3,4,5,6,7]
n=len(array)
target=int(input("Enter the number you want to search \n--->"))
print(LinearSearch(array))
