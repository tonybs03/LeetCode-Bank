class Solution(object):
    def sortedSquares(self, nums):
        result = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                result.append(nums[r]**2)
                r -= 1
            else:
                result.append(nums[l]**2)
                l += 1
        return list(reversed(result))

nums = [-16, -7, -1, 0, 3, 7, 9]
print(Solution().sortedSquares(nums))

# O(n) as it iterates through the whole array (n/2 -> n)
# O(1) for space (constant extra space), if result array is not counted (which it shouldn't)
# Sort the squares of a sorted array 