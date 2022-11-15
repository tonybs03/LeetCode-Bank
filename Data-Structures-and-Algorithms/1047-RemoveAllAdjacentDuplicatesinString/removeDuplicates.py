# Solution using hashmap
from string import ascii_lowercase
class Solution(object):
    def removeDuplicates(self, s):
        # making a hashmap of all lowercase characters
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for d in duplicates:
                s = s.replace(d, '')
        return s

S = 'aabbccioppoil'
print(Solution().removeDuplicates(S))

# O(N^2) for time, because we traverse N times with replace function in each N
# O(N) for space, becasue replace function keeps a copy
# Remove all adjacent repeating elements
