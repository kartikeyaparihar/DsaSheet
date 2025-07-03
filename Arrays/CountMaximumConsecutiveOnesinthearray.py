def CountMaximumConsecutiveOnes(array):
    cnt=0
    maxi=0
    for i in range(n):
        if array[i] == 1:
            cnt+=1  
        else :
            cnt=0      
        maxi = max(maxi,cnt)
    return maxi
array=[1,1,1,1,1,0,1,1,1,1]
n=len(array)
print(CountMaximumConsecutiveOnes(array))