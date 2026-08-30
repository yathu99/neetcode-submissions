class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s)==0:
            return True
        cur=0
        for ind,val in enumerate(t):
            if cur < len(s) and t[ind]==s[cur]:
                cur+=1
        return cur >= len(s)
