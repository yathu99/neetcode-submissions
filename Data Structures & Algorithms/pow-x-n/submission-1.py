class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1.0
        if(n==0):
            return 1
        else:
            for z in range(0,abs(n)):
                res*=x
        if(n<0):
            return 1/res
        return res