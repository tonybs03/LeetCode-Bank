class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        ans = []
        def ioTfn(node):
            if node:
                ioTfn(node.left)
                ans.append(node.val)
                ioTfn(node.right)
    
        ioTfn(root)
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
print(Solution().inorderTraversal(root))

# O(N) where N is the total number of nodes
# O(N) for worst case and O(log2(N)) for best case
# Inorder Traversal