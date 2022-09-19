class Mutations:
    def maxArea(self, h):
        i, j = 0, len(h) - 1
        maxarea = 0
        while i < j:
            width = j-i
            maxarea = max(maxarea, min(h[i], h[j]) * width)
            if h[i] <= h[j]:
                i += 1
            else:
                j -= 1               
        return maxarea

height = [1, 8, 9, 5, 1200, 3, 1900, 300, 25]
print(height)

mutations = Mutations()
print(Mutations().maxArea(height))
print(mutations.maxArea(height))

# O(N) for time (N/2 steps to iterate through)
# O(1) for space (constant extra space, maxarea stores one information)