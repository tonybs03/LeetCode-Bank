class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
            
        return count, nums

nums = [1, 2, 2, 2, 5, 7, 9, 11, 2, 19]
val = 2
print(Solution().removeElement(nums, val))

# O(N)
# O(1) for space (constant extra space)
# remove elements with value val, return number of left over elements