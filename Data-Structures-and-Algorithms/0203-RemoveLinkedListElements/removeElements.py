class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        # create a dummy first so that we can have a prev and a curr pointer
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        # if the curr value is the same as val, then we make prev.next link to the next node of curr
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

LL = ListNode(0)
LL.next = ListNode(1)
LL.next.next = ListNode(2)
LL.next.next.next = ListNode(3)
LL.next.next.next.next = ListNode(4)
LL.next.next.next.next.next = ListNode(5)
node = Solution().removeElements(LL, 0)
while node:
    print(node.val)
    node = node.next
    
# O(N) one pass traverse
# O(1) constant extra space required
# Remove node from a linked list