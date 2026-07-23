class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k=k
        self.arr=nums
        while(len(nums))>k:
            heapq.heappop(self.arr)

        
        



    



    def add(self, val: int) -> int:
        heapq.heappush(self.arr,val)
        if(len(self.arr)>self.k):
            heapq.heappop(self.arr)
        return self.arr[0]
