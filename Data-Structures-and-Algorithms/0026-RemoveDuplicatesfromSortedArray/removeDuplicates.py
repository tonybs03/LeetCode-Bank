class Solution(object):
    def removeDuplicates(self, nums):
        curind = 1
        for i in range(1, len(nums)):       
            if nums[i] != nums[curind-1]:
                nums[curind] = nums[i]
                curind += 1
        print(nums)        
        return (curind)

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))

# O(n)
# O(1)
# Remove repeated elements