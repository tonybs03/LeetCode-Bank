class Solution(object):
    def reverseWords(self, s):
        # all three (split, reverse, and join) operations are O(N), so O(3N) ~= O(N)
        S = reversed(s.split())
        return " ".join(S)

s = " the sky is blue "
print(Solution().reverseWords(s))

# O(N)
# O(N) for space storing the array of s.split()
# Reverse words