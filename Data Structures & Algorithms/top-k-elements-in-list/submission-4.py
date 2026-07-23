class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequents=[] #bounded to size of k elements
        counts={}.fromkeys(set(nums),0)
        for x in range(len(nums)):
            counts[nums[x]]+=1
            if(nums[x] not in frequents and len(frequents)<k):
                frequents.append(nums[x])
            elif(nums[x] not in frequents):
                for y in range(len(frequents)):
                    if(counts[nums[x]]>counts[frequents[y]]):
                        frequents.pop(y)
                        frequents.insert(y,nums[x])
                        break
        return frequents