def recursive_binary_search(array,target):
    if len(array) == 0 :
        return False
    else:
        midpoint = len(array)//2

        if array[midpoint] == target:
            return True
        else:
            if array[midpoint] < target:
                return recursive_binary_search(array[midpoint+1:],target)
            else:
                return recursive_binary_search(array[:midpoint],target)
            
def verify(result):
    print("Target is found:", result)

nums = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(nums,11)
verify(result)