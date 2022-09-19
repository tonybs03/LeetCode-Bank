class Functions(object):
    def longestOnes(self, nums, k):
        curlen = 0
        maxlen = 0
        zeroes = 0
        i = 0

        if len(nums) == 0:
            return 0
        
        for j in range(len(nums)):
            
            if nums[j] == 0:
                zeroes += 1
            
            while i <= j and zeroes > k:
                if nums[i] == 0:
                    zeroes -= 1
                i += 1 
            curlen = j-i+1
            maxlen = max(maxlen, curlen) 

        return maxlen

arr = [0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1]
k = 3
print(arr)
print(Functions().longestOnes(arr,k))


# O(N) for time (N steps to iterate through)
# O(1) for space (constant extra space)