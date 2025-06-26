def find_highest_lowest_frequency(arr):
    freq_map = {}

    # Count frequencies
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Initialize with extreme values
    max_freq = float('-inf')
    min_freq = float('inf')
    max_freq_elem = min_freq_elem = None

    # Find elements with highest and lowest frequency
    for key, value in freq_map.items():
        if value > max_freq:
            max_freq = value
            max_freq_elem = key
        if value < min_freq:
            min_freq = value
            min_freq_elem = key

    return max_freq_elem, min_freq_elem

arr1 = [10, 5, 10, 15, 10, 5]
print(find_highest_lowest_frequency(arr1))  # Output: (10, 15)
