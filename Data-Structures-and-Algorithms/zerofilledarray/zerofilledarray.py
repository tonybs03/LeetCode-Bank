class Functions(object):
    def zeroFilledSubarray(self, nums):
        total = 0
        cur = 0
        
        if len(nums) == 0:
            return 0
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                cur += 1
                
            if nums[i] != 0 or i == (len(nums)-1):
                if cur != 0:
                    total += ((cur+1)*cur/2)
                    cur = 0             
        return total
arr = [0,0,0,2,0,0,2,0,0]
print(arr)
print(Functions().zeroFilledSubarray(arr))

# O(N) for time (N steps to iterate through)
# O(1) for space (constant extra space)
