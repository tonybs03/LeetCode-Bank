class Functions(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            index = i
            comp = target - nums[i]
            for j in range(index+1, len(nums)):   
                if nums[j] == comp:
                    return [i, j]
            
                

arr = [1, 3, 5, 9, 3, 12, -5, 6, 12]
k = 13
print(arr)
print(Functions().twoSum(arr,k))


# O(n^2) for time (n x n steps to iterate through)
# O(1) for space (constant extra space)