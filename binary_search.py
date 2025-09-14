def binary_search(arr,target):
    left,right = 0, len(arr)-1

    while left <= right:
        midpoint = (left+right)//2
        if arr[midpoint] == target:
            return midpoint
        else:
            if arr[midpoint] < target:
                left = midpoint + 1
            else: 
                right = midpoint - 1
    return -1

def verify(result):
    if result == -1:
        print("Target not found")
    else : 
        print("Target found at: ", result)

nums = []
result = binary_search(nums,6)
verify(result)
