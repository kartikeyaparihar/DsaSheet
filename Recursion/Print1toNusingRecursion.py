#Parametr passing approach
def func(count,n):
    if count>n:
        return
    print(count)
    count +=1
    func(count,n)

func(1,15)
    


n=int(input("ENter how many times you want to print"))
count = 1
def func():
    global n 
    global count
    if count>n:
        return
    print(count)
    count +=1
    func()

func()
    