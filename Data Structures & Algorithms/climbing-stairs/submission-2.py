class Solution:
    def climbStairs(self, n: int) -> int:
        n1,n2=1,1
        temp=0
        if(n<3):
            return n
        for x in range(n -1):
            temp = n1
            n1 = n1+n2
            n2 = temp
        return n1





