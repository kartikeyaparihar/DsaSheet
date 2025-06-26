def secondLargestElement(array):
    if len(array)<2:
        return -1
    first=second=float('-inf')
    for num in array:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num
    return second if second!=float('-inf') else None
array=[2,4,5,66,77,55,43,2] 
print("second highest number is ",secondLargestElement(array))