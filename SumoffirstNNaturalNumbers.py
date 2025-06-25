#Loop Approach
def func():
   for i in range(1,n+1):
       sum+=i
       print("totalsum = ",sum)
n=int(input("Enter the number till you want the sum"))
func()
    
    
#formula approach time 0(1)
def func(n):
    sum=n*(n+1)//2
    print("Sum is = ",sum)
func(5)

