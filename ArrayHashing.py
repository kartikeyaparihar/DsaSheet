array = [1,2,1,2,4,6]
#pre storing
hash_array = [0]*13 #Assuming max is 12
for num in array:
    hash_array[num]+=1
#queries
queries=[1,2,8,7,10,12,4]
for q in queries:
    print(hash_array[q],end=" ")