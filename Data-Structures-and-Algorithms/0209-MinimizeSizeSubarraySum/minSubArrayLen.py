class Solution(object):
    def minSubArrayLen(self, nums, target):
        ans = float("inf")
        cursum = 0
        left = 0
        right = 0
        for i in range(len(nums)):
            right = i   
            cursum += nums[i]
            while cursum >= target and left <= right:
                ans = min(right - left + 1, ans)
                cursum -= nums[left]
                left += 1       
        return 0 if ans == float("inf") else ans

nums = [2, 3, 1, 2, 4, 3, 1, 2, 1, 2, 4]
target = 500
print(Solution().minSubArrayLen(nums, target))

# O(n) single iteration through n elements
# O(1) for space (constant extra space)
# Return minimal length of continuous elements with sum bigger and equal to the target
