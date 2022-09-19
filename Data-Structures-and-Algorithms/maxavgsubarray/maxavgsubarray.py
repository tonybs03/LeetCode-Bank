class Functions(object):
    def findMaxAverage(self, nums, k):
        maxsum = 0
        cursum = 0
        for i in range(k):
            cursum += nums[i]
        maxsum = cursum
        for j in range(k, len(nums)):
            cursum += nums[j]- nums[j-k]
            maxsum = max(cursum, maxsum)
        return maxsum*1.0/k
        

    
arr = [-1,2,-4]
k = 2
print(arr)
print(Functions().findMaxAverage(arr,k))


# O(N) for time (N steps to iterate through)
# O(1) for space (constant extra space)