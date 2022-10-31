class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteNode(self, node):
        curr = node
        curr.val = curr.next.val
        curr.next = curr.next.next

LL = ListNode(0)
deletenode = LL.next = ListNode(1)
LL.next.next = ListNode(2)
LL.next.next.next = ListNode(3)
LL.next.next.next.next = ListNode(4)
LL.next.next.next.next.next = ListNode(5)
print(Solution().deleteNode(deletenode))
node = LL
while node:
    print(node.val)
    node = node.next

# O(1)
# O(1)
# Given a node, delete it from the linked list guranteed that it is not the last node