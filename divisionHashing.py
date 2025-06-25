arr = [2, 5, 16, 28, 139]
hash_size = 10
hash_table = [[] for _ in range(hash_size)]  # 10 buckets

# Pre-storing
for num in arr:
    index = num % hash_size
    hash_table[index].append(num)

# Fetching
def get_frequency(hash_table, num):
    index = num % hash_size
    return hash_table[index].count(num)

queries = [5, 16, 100]
for q in queries:
    print(get_frequency(hash_table, q), end=" ")