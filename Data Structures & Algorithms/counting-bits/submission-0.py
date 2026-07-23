class Solution:
    def countBits(self, n: int) -> List[int]:
        nums=[]
        for x in range(0,n+1):
            nums.append(bin(x).count('1'))
        return nums