class Solution:
    def decodeString(self, s):
        # initiate the stack that stores strings and the number of repeats for them
        stack = []
        # we observe that after digits must come an opening bracket
        curstr = ''
        curnum = 0
        # traverse through the string
        for char in s:
            # if it is a digital number 
            if char.isdigit():
                curnum = curnum*10 + int(char)
            # after a number comes the opening bracket, we save the number and the string in stack
            elif char == "[":
                stack.append((curnum, curstr))
                curnum = 0
                curstr = ''
            # append to string if it is a letter
            elif char.isalpha():
                curstr += char
            # if it is a closing bracket, we pop the letters in stack
            elif char == "]":
                savednum, savedstr = stack.pop()
                curstr = savedstr + savednum*curstr
        return curstr

string = '3[a2[c]]'  #accaccacc
print(Solution().decodeString(string))

# O(maxK*n) max digit times the length of the longest strinfg
# O(N+M) storing in stack 
# Decoding a string 