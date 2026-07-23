class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def next_level(subset,cur,iters=[]):
            if(sum(subset) == target):
                res.append(subset.copy())
            if(sum(subset) > target):
                return  
            if(sum(subset) < target):
                for i in range(cur,len(iters)):
                    subset.append(iters[i])
                    if(sum(subset) > target):
                        break   
                    next_level(subset.copy(),i,iters)
                    subset.pop()
        next_level([],0,nums)
        return res
                