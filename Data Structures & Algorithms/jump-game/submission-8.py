class Solution:
    def canJump(self, nums: List[int]) -> bool:
        checks = [False for x in range(len(nums))]
        checks[-1]=True
        for z in range(len(nums)-2,-1,-1):
            checker=z+1
            while(checker <= z+nums[z] and checker < len(nums) or not (checks[checker])):
                if checks[checker]:
                    checks[z]=True
                    break
                checker+=1
        return checks[0]
