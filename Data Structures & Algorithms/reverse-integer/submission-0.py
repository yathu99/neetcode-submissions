class Solution:
    def reverse(self, x: int) -> int:
        data=2147483647
        if(x==0):
            return 0
        neg=1 if x>0 else -1
        return 0 if int(str(abs(x))[::-1])>data or int(str(abs(x))[::-1]) < -data else int(str(abs(x))[::-1])*neg