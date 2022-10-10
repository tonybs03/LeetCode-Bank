import numpy as np

class Solution(object):
    def minimumAverageDifference(self, nums):
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        ans = 10000000000000000000000000000
        index = 0
        for i in range(0, len(nums)):
            a = prefix[i]
            b = i+1
            c = prefix[-1]-prefix[i]
            d = len(nums)-(i+1)
            if d == 0:
                res = np.abs(a/b)
            else: 
                res = np.abs(a/b - c/d)
            if res < ans:
                ans = res
                index = i
        
        return index
        