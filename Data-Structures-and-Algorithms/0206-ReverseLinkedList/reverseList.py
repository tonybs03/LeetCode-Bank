class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        # singly linked, each node has .next and .val. The goal is to link the next nodes in reverse order.
        newnext = None   
        curnode = head

        while curnode:
            temp = curnode.next   #temp is the rest part of the curr
            curnode.next = newnext   #first loop newnext = None, for the last element in the linked list should have a .next property of None
            #updates the newnext to curr and curr to temp which is curr.next, moves the while loop till curr = temp = undefined for the last element
            newnext = curnode   
            curnode = temp

        return newnext 

LL = ListNode(0)
LL.next = ListNode(1)
LL.next.next = ListNode(2)
LL.next.next.next = ListNode(3)
LL.next.next.next.next = ListNode(4)
LL.next.next.next.next.next = ListNode(5)
node = Solution().reverseList(LL)
while node:
    print(node.val)
    node = node.next
    
# O(N) one pass traverse
# O(1) constant extra space required
# Reverse the linked list