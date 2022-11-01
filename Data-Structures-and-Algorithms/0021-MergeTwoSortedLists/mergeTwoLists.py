class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # basic cases
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        # initiate a dummy head first
        dummyhead = ListNode(0)
        ins = dummyhead
        # while both of these are not none yet
        while l1 and l2:
            # attach the smaller valued l1 node to the dummyhead, and move l1 to the next node 
            if l1.val <= l2.val:
                ins.next = l1
                l1 = l1.next
            # attach the smaller valued l2 node to the dummyhead, and move l2 to the next node            
            else:
                ins.next = l2
                l2 = l2.next
            # after each insertion, we move the insertion point ins to the most recently added node so that the 
            # next time an insertion happens, it actually inserts at the right place
            ins = ins.next

        # in case the lengths are different between two lists, we attach whichever one that is not empty 
        ins.next = l1 if l1 is not None else l2

        # then, we return the dummyhead.next. We cannot use ins becasue ins is the writer.
        return dummyhead.next

L1 = ListNode(1)
L1.next = ListNode(1)
L1.next.next = ListNode(2)
L1.next.next.next = ListNode(3)
L1.next.next.next.next = ListNode(5)
L1.next.next.next.next.next = ListNode(6)

L2 = ListNode(1)
L2.next = ListNode(2)
L2.next.next = ListNode(3)
L2.next.next.next = ListNode(4)
L2.next.next.next.next = ListNode(5)
L2.next.next.next.next.next = ListNode(7)

node = Solution().mergeTwoLists(L1, L2)
while node:
    print(node.val)
    node = node.next
    
# O(N+M) one pass traverse through each list
# O(1) constant extra space required for dummyhead and there is no recursion
# Merge two sorted Nodelists in a sorted fashion