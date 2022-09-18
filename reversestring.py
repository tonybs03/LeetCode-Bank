class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s

arr = ["h","e","l","l","o"]
arr2 = Solution()
arr2 = arr2.reverseString(arr)
print(arr2)