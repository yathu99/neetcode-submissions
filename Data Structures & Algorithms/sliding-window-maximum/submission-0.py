class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k
        ans=[]
        if k >= len(nums):
            return [max(nums)]
        else:
            for m in range(len(nums)-k+1):
                ans.append(max(nums[m:m+k]))
        return ans