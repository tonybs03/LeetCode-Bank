class Solution(object):
    def isHappy(self, n):
        seen_before = set()

        while n != 1:
            n = sum([int(d)**2 for d in str(n)])
            if n in seen_before:
                return False
            else:
                seen_before.add(n)
        
        return True

n = 19
print(Solution().isHappy(n))

# O(logn) with log base of 10 (number of digits scales in log10 with the number)
# O(logn) for space
# Sum of each digit squared of a number, recursive, until number is 1 

