class Solution:
    def isValid(self, s: str) -> bool:
        ins = {'(':')','{':'}','[':']'}
        word=[]
        for x in s:
            if (x in ins.keys()):
                word.append(x)
            elif (len(word)>0 and x==ins.get(word[len(word)-1])):
                word.pop(-1)
            else:
                return False
        if(len(word)==0):
            return True
        return False
