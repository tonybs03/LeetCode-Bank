class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2   #// is a flooring division
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1

nums = [3, 7, 11, 15, 21, 91, 125, 786, 1230]
target = 125
print(Solution().search(nums, target))

# O(logN) with log base 2
# O(1) for space (constant extra space)