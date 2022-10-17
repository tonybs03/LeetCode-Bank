class Solution(object):
    def intersection(self, nums1, nums2):
            nums1.sort()
            nums2.sort()
            i = j = 0
            ans = []

            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    i += 1
                elif nums1[i] > nums2[j]:
                    j += 1
                else:
                    if len(ans) == 0 or nums1[i] != ans[-1]:
                        ans.append(nums1[i])
                    
                    i += 1
                    j += 1
                    
            return ans

nums1 = [3, 7, 11, 15, 21, 91, 125, 786, 1230] #len=m
nums2 = [5, 7, 0, 8, 12, 156, 78, 11, 3] #len=n
print(Solution().intersection(nums1, nums2))

# O(mlogm + nlogn) (or O(n)???)
# O(1) for space (constant extra space for ans doesn't count)
# Search the same values from two arrays and return them