def Findthenumberthatappearsonce(array):
    hashmap={}
    for i in array:
        hashmap[i]=hashmap.get(i,0)+1
    for num , count in hashmap.items():
        if count==1:
            return num
    return array
array=[1,1,2,3,4,2,4]
n=len(array)
print(Findthenumberthatappearsonce(array))