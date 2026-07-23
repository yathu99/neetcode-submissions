class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        global answer
        answer=[]

     
        def chooseElem(selected,pool):
            lastPool=pool.copy()
            if len(pool)==0 or len(selected) >= len(nums):
                answer.append(selected)
            for index in range(len(pool)):
                newSelect=selected.copy()
                newPool = lastPool.copy()
                newSelect.append(newPool[index])
                newPool.pop(index)
                chooseElem(newSelect,newPool)
        chooseElem([],nums)
        return answer
