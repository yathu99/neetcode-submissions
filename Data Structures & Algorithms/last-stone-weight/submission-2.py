class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while(len(stones)>1):
            [one,two]=heapq.nlargest(2,stones)
            stones.remove(one)
            stones.remove(two)
            if(one!=two):
                heapq.heappush(stones,abs(one-two))
            else:
                if(len(stones)==0):
                    return 0
        return stones[0]
