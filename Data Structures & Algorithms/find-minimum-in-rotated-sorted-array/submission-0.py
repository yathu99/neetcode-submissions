class Solution:
    def findMin(self, nums: List[int]) -> int:
        lastMin=nums[0]
        for x in range(len(nums)-1):
            if(lastMin>nums[x+1]):
                lastMin=nums[x+1]
                return lastMin
            if(lastMin<nums[x+1]):
                continue
        return lastMin
