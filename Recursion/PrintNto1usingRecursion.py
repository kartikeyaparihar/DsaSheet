def func(count,n):
    if count>n:
        return
    print(n)
    n-=1
    func(count,n)

func(1,15)
