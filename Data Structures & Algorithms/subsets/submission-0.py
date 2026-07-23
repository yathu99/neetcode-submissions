class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        prevArr=last_level=[[]]
        for x in nums:
            prevArr=last_level.copy()
            number=x
            for elem in prevArr:
                newElem=elem.copy()
                newElem.append(number)
                last_level.append(newElem)
        return last_level
                
