class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid -1
       
        return l


nums = [3, 7, 11, 15, 21, 91, 125, 786, 1230]
target = 126
print(Solution().searchInsert(nums, target))

# O(logN) with log base 2
# O(1) for space (constant extra space)