class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri=[[1 for y in range(x+1)] for x in range(numRows)]
        for x in range(2,numRows):
            for y in range(1,x):
                tri[x][y]=tri[x-1][y-1]+tri[x-1][y]
        return tri
        
