function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

const mergeTwoLists = function(list1, list2) {
    if (!list1) {
        return list2
    }
    if (!list2) {
        return list1
    }

    let head;
    if (list1.val <= list2.val) {
        head = list1;
        list1 = list1.next
    } else {
        head = list2;
        list2 = list2.next
    }

    head.next = mergeTwoLists(list1, list2)

    return head
};

let L1 = new ListNode(1)
L1.next = new ListNode(1)
L1.next.next = new ListNode(2)
L1.next.next.next = new ListNode(3)
L1.next.next.next.next = new ListNode(5)
L1.next.next.next.next.next = new ListNode(6)

let L2 = new ListNode(1)
L2.next = new ListNode(2)
L2.next.next = new ListNode(3)
L2.next.next.next = new ListNode(4)
L2.next.next.next.next = new ListNode(5)
L2.next.next.next.next.next = new ListNode(6)
node = mergeTwoLists(L1, L2)
while (node) {
    console.log(node.val)
    node = node.next
}

// O(N+M) one pass traverse through each list
// O(N+M) comes with recursion
// Merge two sorted Nodelists in a sorted fashion