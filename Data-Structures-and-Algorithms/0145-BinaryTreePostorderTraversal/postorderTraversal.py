class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Use iteration method 
class Solution(object):
    def postorderTraversal(self, root):
        stack = []
        res = []
        node = root
        # The idea is that push each node twice, only push the val after the third visit, for the first visit appends twice, second visit checks right side, third visit pushes the val
        while node or stack:
            # if node does exist, we stack it twice and move left
            if node:
                stack.append((node, True))
                stack.append((node, False))
                node = node.left
            # traverse left till null, then go back the leaf
            if node == None:
                node, visited = stack.pop()             
                if visited:
                    res.append(node.val)
                    node = None
                else:
                    node = node.right
        return res

root  = TreeNode(0)
one   = TreeNode(1)
two   = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
root.left = one
root.right = two
two.right = four
four.left = three
print(Solution().postorderTraversal(root))

# O(N) where N is the total number of nodes
# O(N) for worst case and O(log2(N)) for best case
# Postorder Traversal