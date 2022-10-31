function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

const deleteNode = function(node) {
    node.val = node.next.val;
    node.next = node.next.next;
};

let LL = new ListNode(0);
LL.next = new ListNode(1);
LL.next.next = new ListNode(2);
let deletenode = LL.next.next.next = new ListNode(3);
LL.next.next.next.next = new ListNode(4);
LL.next.next.next.next.next = new ListNode(5);
deleteNode(deletenode);
node = LL;
while (node) {
    console.log(node.val);
    node = node.next;
};
    
// O(1)
// O(1)
// Given a node, delete it from the linked list guranteed that it is not the last node