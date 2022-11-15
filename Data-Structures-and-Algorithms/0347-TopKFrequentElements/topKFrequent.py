# i need the dict function from collections and I am going to use bucketlist
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        # we cannot sort for sorting violates the complexity
        # initiate a dictionary with integer type 
        myhash = collections.defaultdict(int)

        # because k is in the range of 1 to number of unique numbers
        if len(nums) == k:
            return nums

        # add nums and their counts into the dict
        for n in nums:
            myhash[n] += 1

        # initiate a bucketlist that uses index as count (elements in the 0th list has a count of 1)
        bucketlist = [[] for i in range(len(nums))]
        for number, count in myhash.items():
            bucketlist[count-1].append(number)
        print(bucketlist)

        # put everything into a stack, and the last bucket which has the highest counts for numbers therein will be at the end of the stack...
        finalist = []
        for bucket in bucketlist:
            finalist.extend(bucket)
        print(finalist)

        # return the last k elements in the list
        res = finalist[-k:]

        return res   

nums = [1, 1, 1, 1, 4, 5, 6, 7, 5, 6, 8, 1, 4, 5, 0, 1, 2, 5, 0, 5, 5, 5, 5, 5, 5, 5, 6]
k = 3
print(Solution().topKFrequent(nums, k))

# O(N) for time, because we traverse through the iteration for multiple times but never nested within each other
# O(N) for space for similar reasons
# Top K numbers with the most appearences
