class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater=0
        start,end=0,len(heights)-1
        while(start < end ):
            res = min(heights[start],heights[end]) * (end-start)
            maxWater = max(res,maxWater)
            if(heights[start]<=heights[end]):
                
                start+=1
            else:
                end-=1
        return maxWater   