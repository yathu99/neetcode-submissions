import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0]>target:
            return False
            
        l=bisect.bisect_left([matrix[x][0] for x in range(len(matrix))],target)
        
        if l>=0 and l<len(matrix) and matrix[l][0] == target:
            return True
        
        ans=bisect.bisect_left(matrix[l-1],target)
        if ans>0 and ans<len(matrix[0]) and matrix[l-1][ans]==target:
            return True
        return False