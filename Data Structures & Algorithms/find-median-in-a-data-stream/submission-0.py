class MedianFinder:

    def __init__(self):
        self.leftMaxHeap=[]
        self.rightMinHeap=[]
        self.lastMin=0

    def addNum(self, num: int) -> None:
        # if len(self.leftMaxHeap) == len(self.rightMinHeap) == 0:
        #     heapq.heappush_max(self.leftMaxHeap,num)
        #     self.leftMaxHeap=self.lastMin
        #     return

        # if num > self.lastMin:
        #     if len(self.leftMaxHeap) - len(self.rightMinHeap) < 2: 
        #         heapq.heappush(self.rightMinHeap,num)

        # else:
        #     heapq.heappush_max(self.leftMaxHeap,num)

        if (len(self.leftMaxHeap)==len(self.rightMinHeap)):
            heapq.heappush_max(self.leftMaxHeap, heapq.heappushpop(self.rightMinHeap, num))
        else:
            heapq.heappush(self.rightMinHeap, heapq.heappushpop_max(self.leftMaxHeap, num))
        
        
    def findMedian(self) -> float:
        if len(self.rightMinHeap) == len(self.leftMaxHeap):
            return (self.leftMaxHeap[0]+self.rightMinHeap[0])/2
        else:
            return self.leftMaxHeap[0]
        