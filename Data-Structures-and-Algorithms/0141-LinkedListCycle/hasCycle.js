function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

const hasCycle = function(head) {
    // if the head is empty, we immediately return False
    if ( head == null ) {
        return false;
    };

    // use two runners, one fast and one slow
    var slow = head;
    var fast = head.next;
    // if by the time when fast catches up to slow in the next cycle, we return true and stop the loop
    while ( slow != fast ) {
        // if we find a node that is null, we know it is not a cycle
        if ( fast == null || fast.next == null) {
            return false;
        }
        // update the runners 
        slow = slow.next;
        fast = fast.next.next;
    };
    
    return true
};

let LL = new ListNode(0)
LL.next = new ListNode(1)
LL.next.next = new ListNode(2)
LL.next.next.next = new ListNode(3)
LL.next.next.next.next = new ListNode(4)
LL.next.next.next.next.next = new ListNode(5)
LL.next.next.next.next.next.next = LL
console.log(hasCycle(LL))

// O(N)
// O(1) n
// Is it a cycle?