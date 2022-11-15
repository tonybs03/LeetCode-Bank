# for using list implementation using stacks, we can only use pop or push for same-end mutations
class MyQueue(object):
    def __init__(self):
        self.main = []
        self.helper = []

    # use main list for appending at the end
    def push(self, x):
        self.main.append(x)
        
    def pop(self):
        # put all main elements into the helper stack using pop (from the end)
        while self.main:
            self.helper.append(self.main.pop())
        # result returning the last element of helper, which was the first element of main
        res = self.helper.pop()
        # then, we push everything from helper to main again
        while self.helper:
            self.main.append(self.helper.pop())
        return res

    def peek(self):
        # put all main elements into the helper stack using pop (from the end)
        while self.main:
            self.helper.append(self.main.pop())
        if len(self.helper):
            res = self.helper[-1]
        else:
            res = 'empty list'
        while self.helper:
            self.main.append(self.helper.pop())
        return res

    def empty(self):
        return len(self.main) == 0
        
obj = MyQueue()
obj.push(3)
obj.push(6)
obj.push(9)
param_1 = obj.pop()
param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()
param_5 = obj.pop()
param_6 = obj.empty()
print(param_1)
print(param_2)
print(param_3)
print(param_4)
print(param_5)
print(param_6)