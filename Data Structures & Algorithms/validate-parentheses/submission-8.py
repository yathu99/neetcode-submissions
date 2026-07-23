class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)<2):
            return False
        brackets_open={
            91:93,
            123:125,
            40:41
        }
        brackets_closed={
            93:91,
            125:123,
            41:40
        }

        stack=[]
        pointer=0
        while pointer<len(s):
            if(ord(s[pointer]) in brackets_open.keys()):
                stack.append(s[pointer])
            else:
                if(ord(s[pointer]) in brackets_closed.keys()):
                    if(len(stack)<1):
                        return False
                    if(ord(stack[-1]) != brackets_closed[ord(s[pointer])]):
                        return False
                    else:
                        stack.pop()
            pointer+=1
        if(len(stack)>0):
            return False
        return True
            