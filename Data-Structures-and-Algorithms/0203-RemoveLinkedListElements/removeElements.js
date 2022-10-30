function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

const removeElements = function(head, val) {
    // return head if head is empty
    if (!head) {return head}
    // remove leading nodes with val equal to target val
    while( head && head.val == val ) {
        head = head.next;
    }
    // use a pointer
    let curr = head;
    // while curr is not null
    while (curr) {
        // use next as the next node
        let next = curr.next
        // if the next node is target val, we keep skipping (reasign next as next.next) until next has no leading target vals
        while ( next && next.val == val ) {
            next = next.next
        }
        // with a clean leading next ListNodes, we basically attach it to curr, and then foward curr to curr.next to move along the while (curr) loop
        curr.next = next
        curr = curr.next
    }
    return head
};

let LL = ListNode(0)
LL.next = ListNode(1)
LL.next.next = ListNode(2)
LL.next.next.next = ListNode(3)
LL.next.next.next.next = ListNode(4)
LL.next.next.next.next.next = ListNode(5)

// # O(N) one pass traverse
// O(1) constant extra space required
// Remove node from a linked list