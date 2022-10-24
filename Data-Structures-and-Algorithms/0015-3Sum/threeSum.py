class Solution(object):
    def threeSum(self, nums):
        # sorting so that anything above 0 is discarded (impossible to make a zero out of only positive numbers)
        nums.sort()   #O(N*logN)
        res = []
       
        for i in range(len(nums)):
            # if the number is above 0, we break this outer for loop
            if nums[i] > 0:
                break
            # if the negative is unique from previous element value, we run the twoSum function that finds the complement
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, i, res): 
        # create a set, which records numbers to the right of nums[i]
        seen = set()
        # start with i + 1, to find more pairs with -nums[i]
        j = i + 1
        while j < len(nums):
            # if comp is in seen set, then we know the comp, the nums[i], and the nums[j] is a triplet.
            comp = -(nums[i]+nums[j])
            if comp in seen:
                res.append([nums[i], nums[j], comp])
                # if the j+1 element is the same as the j element, we skip
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            # this way, the numbers won't be repeated because it is a set, and the returns won't repeat itself
            seen.add(nums[j])
            j += 1

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

# O(N^2) since it has two full loops (almost) within one another
# O(N) stores hashset of size N
# Array of numbers with negative and positive values, find the threeSum that is zero