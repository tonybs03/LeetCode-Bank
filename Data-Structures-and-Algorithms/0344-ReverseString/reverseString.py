class Mutations:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s

arr = ["h","e","l","l","o"]
print(arr)

mutations = Mutations()
mutations.reverseString(arr)
print(arr)

# O(N) for time (N/2 swaps)
# O(1) for space (no recursion)
# Two pointer, left end and right end, move inwards.