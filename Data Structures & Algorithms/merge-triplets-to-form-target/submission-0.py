class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valids=[]
        for trip in triplets:
            if trip[0]<=target[0] and trip[1]<=target[1] and trip[2]<=target[2]:
                valids.append(trip)
        ans=[False,False,False]
        for triplet in valids:
            for ind in range(3):
                if triplet[ind]==target[ind]:
                    ans[ind]=True
        return all(ans)

