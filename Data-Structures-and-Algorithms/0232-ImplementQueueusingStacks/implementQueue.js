// for linked list implementation, we create the Node function first
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

// initializing the queue
const MyQueue = function() {
    this.queue = new ListNode(0)
    this.cur = this.queue
    this.length = 0
};

// make the current node point to the next node with the x value and move cursor to the newest node, and add length
MyQueue.prototype.push = function(x) {
    this.cur.next = new ListNode(x)
    this.cur = this.cur.next
    this.length++
};

// if the queue has been initialized, and if there has been a pushed element (queue.next), we can then pop it out.
MyQueue.prototype.pop = function() {
    if(this.queue && this.queue.next) {
        // return this res as the front of the queue
        const res = this.queue.next.val
        // remove the "first node", this.queue.next is always the front even though we have the 0 node as a leading reference node
        this.queue = this.queue.next
        this.length--
        return res
    }
};

// return the front node value
MyQueue.prototype.peek = function() {
    if(this.queue && this.queue.next) {
        const res = this.queue.next.val        
        return res
    } 
};

MyQueue.prototype.empty = function() {
    return this.length === 0
};

var obj = new MyQueue()
obj.push(3)
obj.push(6)
var param_2 = obj.pop()
var param_3 = obj.peek()
var param_4 = obj.empty()
console.log(obj)
console.log(param_2)
console.log(param_3)
console.log(param_4)

// Implementing a queue stack with linked list