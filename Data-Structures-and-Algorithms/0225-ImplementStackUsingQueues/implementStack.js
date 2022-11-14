const MyStack = function() {
    this.queue = [];    
};

// pushing to the end is allowed
MyStack.prototype.push = function(x) {
    this.queue.push(x);
    let i  =  0;
    while ( i < this.queue.length - 1) {
        this.queue.push(this.queue.shift())
        i++
    }
};

// we can only use shift as a popleft function of a queue
MyStack.prototype.pop = function() {
    return this.queue.shift()
};

MyStack.prototype.top = function() {
    return this.queue[0]
};

MyStack.prototype.empty = function() {
    return this.queue.length === 0
};

obj = new MyStack()
obj.push(3)
obj.push(6)
obj.push(9)
var param_1 = obj.pop()
var param_2 = obj.top()
var param_3 = obj.pop()
var param_4 = obj.empty()
var param_5 = obj.pop()
var param_6 = obj.empty()
console.log(param_1)
console.log(param_2)
console.log(param_3)
console.log(param_4)
console.log(param_5)
console.log(param_6)