def Bs(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        midpoint = (left +  right)//2

        if array[midpoint] == target:
            return midpoint
        if array[midpoint] < target:
            left = midpoint + 1
        else: 
            right = midpoint -1
    return -1
    
list = [1,2,3,4,5,6,7,8,9,10,11,12]

result = Bs(list,11)

if result == -1:
    print("Target not in the array")
else:
    print("Target found at index: ", result)