def missingNumber(array, N):
    summation = (N * (N + 1)) // 2
    for i in range(N):
       s2 = sum(array)

       missingNum = summation - s2
    return missingNum

array = [1, 2, 4,5]
N = len(array)+1
ans = missingNumber(array, N)
print("The missing number is:", ans)