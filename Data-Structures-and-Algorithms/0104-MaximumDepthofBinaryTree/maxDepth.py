class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        stack = [(root, 1)]
        ans = 0
        while stack:
            node, level = stack.pop()
            ans = max(ans, level)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
                
        return ans

root  = TreeNode(0)
one   = TreeNode(1)
two   = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
root.left = one
root.right = two
two.right = three
three.right = four
print(Solution().maxDepth(root))

# O(N) where N is the total number of nodes
# O(N) for worst case and O(log2(N)) for best case
# Max depth of a binary tree