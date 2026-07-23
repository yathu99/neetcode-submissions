class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data=[]
        for z in points:
            heapq.heappush(data,(z[0]**2 + z[1]**2,z))
        rats=heapq.nsmallest(k,data)
        answers=[x[1] for x in rats]
        return answers