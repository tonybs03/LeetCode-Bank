import collections

class Solution(object):
    def totalFruit(self, fruits):
        basket = collections.defaultdict(int)
        left = 0
        ans = 0

        if len(fruits) < 2:
            return 1

        for right in range(len(fruits)):
            basket[fruits[right]] += 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                left += 1  
            ans = max(ans, right - left + 1)          
        return ans

fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(Solution().totalFruit(fruits))

# O(n) iteration through the whole array
# O(n) dictionary needed space to save information in basket
# Longest continuous subarray with 2 distinct values