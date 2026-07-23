class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pal=set()
        for x in nums:
            if(x in pal):
                return x    
            else:
                pal.add(x)
        