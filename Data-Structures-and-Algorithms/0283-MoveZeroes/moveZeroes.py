class Solution(object):
    def moveZeroes(self, nums):
        left=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left] = nums[i]
                left+=1
        for j in range(left, len(nums)):
            if nums[j] != 0:
                nums[left] = 0
            left+=1   
        return nums


nums = [0,0,1,2,0,5,6,9,14,12,0,1,0]
print(Solution().moveZeroes(nums))

# O(2N) ~= O(N)
# O(1)
# Move zeroes to the end of the array