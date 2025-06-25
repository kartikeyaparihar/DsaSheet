#n=int(input("ENter how many times you want to print"))
#count = 1
def func(count,n):
    #global n 
    #global count
    if count>n:
        return
    print(count)
    count +=1
    func(count,n)
#n=int(input("ENter how many times you want to print"))

func(1,15)
    