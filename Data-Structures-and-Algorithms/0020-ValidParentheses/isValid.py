class Solution(object):
    def isValid(self, s):
        if len(s) < 2:
            return False
        stack = []
        for char in s:
            # if its first character and it is a closing bracket, return false
            if len(stack) == 0:
                if char == ')' or char == '}' or char == ']':
                    return False

            # append opening ones to the stack
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            
            # if i encounter a closing bracket, i check the last element of the stack
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False 
        if len(stack) != 0:
            return False
        return True

gs = '()()(){}{}{}[][][]'
bs = '()()(){}{}{}[][][}'
print(Solution().isValid(gs))
print(Solution().isValid(bs))

# O(N) one pass traverse
# O(N) storing stack for the res is just a boolean
# Are the brackets closed properly?