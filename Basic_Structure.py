count = 0
def func():
    global count #to specify it is global otherwise we cannot put it inside the fun() as it will initialize count as 0 for every func call
    if count == 3: #base condition of the recursion to stop
        return 
    print(count)
    count +=1
    func()   #recursive call

func() #initially calls the fuction