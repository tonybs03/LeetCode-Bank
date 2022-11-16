class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        ans = []
        def pTfn(node):
            if node:
                ans.append(node.val)
                pTfn(node.left)
                pTfn(node.right)
    
        pTfn(root)
        return ans

root  = TreeNode(0)
one   = TreeNode(1)
two   = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
root.left = one
root.right = two
two.right = four
four.right = three
print(Solution().preorderTraversal(root))

# O(N) where N is the total number of nodes
# O(N) for worst case and O(log2(N)) for best case
# Preorder Traversal