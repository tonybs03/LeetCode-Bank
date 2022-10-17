class Solution(object):
    def isPerfectSquare(self, num):
        i = 1
        while i*i <= num:
            if float(num)/float(i) == i:
                return True, i, num
            i += 1
        return False
num = 196
print(Solution().isPerfectSquare(num))

# O(n) 
# O(1) for space (constant extra space)
# Determine the validity of a number in terms of being a perfect square