class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid=False
        allowed="QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        newString=""
        for x in s:
            if(x.upper() in allowed):
                newString+=x.upper()
        s=newString
        start=0
        end=len(s)-1
        while(start<=end and start!=end):
            if(s[start].upper()!=s[end].upper()):
                return False
            start+=1
            end-=1
        return True
