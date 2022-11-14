import collections

class MyStack(object):
    def __init__(self):
        #implementation using queue
        self.main = collections.deque()
        self.helper = collections.deque()
    def push(self, x):
        self.main.append(x)
        #after each appending, we pop all previous elements and attach them behind the newly added element which creates a reverse order queue
        for _ in range(len(self.main) - 1):
            self.main.append(self.main.popleft())
    def pop(self):
        return self.main.popleft()
    def top(self):
        return self.main[0]
    def empty(self):
        return not len(self.main)

obj = MyStack()
obj.push(3)
obj.push(6)
obj.push(9)
param_1 = obj.pop()
param_2 = obj.top()
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