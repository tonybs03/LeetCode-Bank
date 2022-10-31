function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

const reverseList = function(head) {
    // finding the last node
    if ( !head || !head.next ) {
        return head
    }

    // set p as the last node, and then change the .next property of the node
    p = reverseList(head.next)
    head.next.next = head;
    head.next = null;
    return p
};

let LL = new ListNode(0)
LL.next = new ListNode(1)
LL.next.next = new ListNode(2)
LL.next.next.next = new ListNode(3)
LL.next.next.next.next = new ListNode(4)
LL.next.next.next.next.next = new ListNode(5)
node = reverseList(LL)
while (node) {
    console.log(node.val)
    node = node.next
}

// # O(N) one pass traverse
// O(N) for recursion
// Reverse the linked list