class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)*(len(nums)+1)/2
        for z in nums:
            total -= z
        return int(total)

