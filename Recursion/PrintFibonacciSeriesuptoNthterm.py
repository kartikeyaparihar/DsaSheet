def fibonacci_recursive(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
n=int(input("Enter the no.\n----->"))
for i in range(n+1):
    print(fibonacci_recursive(i),end=" ")
