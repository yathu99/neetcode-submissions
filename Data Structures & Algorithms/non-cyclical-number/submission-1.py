class Solution:
    def isHappy(self, n: int) -> bool:
        newSets=set()
        num=n
        while(num not in newSets):
            newSets.add(num)
            lastsum=0
            if(num==1):
                return True
            while(num):
                last=num%10
                num=num//10
                if(last==0):
                    continue
                lastsum+=last**2
            num=lastsum
        if(num==1):
            return True
        return False