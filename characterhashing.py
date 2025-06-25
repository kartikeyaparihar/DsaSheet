char ='ababccdbadf'
hash_char={}
for ch in char:
  hash_char[ch]=hash_char.get(ch,0)+1

queries=['a','b','c','d','f']
for ch in queries:
  print(hash_char.get(ch,0),end=" ")
