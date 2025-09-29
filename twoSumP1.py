def two_sum(array, target):
    seen = {}

    for i in range(len(array)):
        seen[array[i]] = i

    for i in range(len(array)):
        y = target - array[i]

        if y in seen and seen[y] != i:
            return [i,seen[y]]
        
print(two_sum([0,2,3,4,7], 5))