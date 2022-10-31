class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        # use extra N space to save hashset of seen values
        nodes_seen = set()
        # when head is None, we know we are at the end of the linked list, and we stop the loop
        while head is not None:
            # return true for the node has been reached before
            if head in nodes_seen:
                return True
            # if it is a new node, then add to the set
            nodes_seen.add(head)
            print(head.val)
            # move to the next node till it is null 
            head = head.next
        return False

LL = ListNode(0)
LL.next = ListNode(1)
LL.next.next = ListNode(2)
LL.next.next.next = ListNode(3)
LL.next.next.next.next = ListNode(4)
LL.next.next.next.next.next = ListNode(5)
print(Solution().hasCycle(LL))

# O(N) one pass traverse
# O(N) constant extra space required
# Is it a cycle?