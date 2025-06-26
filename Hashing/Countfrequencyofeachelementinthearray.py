#Using Hashmap
def countFreqMap(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for key, value in freq.items():
        print(f"{key} repeated, {value} times")

# Example usage
arr = [10, 5, 10, 15, 10, 5]
countFreqMap(arr)