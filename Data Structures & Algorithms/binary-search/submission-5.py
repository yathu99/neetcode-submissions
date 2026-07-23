class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r=0,n
        mid=(r-l)//2
        while(l<r):
            if(nums[mid] == target):
                return mid
            if(nums[mid]<target):
                l = mid+1
            if(nums[mid]>target):
                r = mid
            mid = l+(r-l)//2
        return -1
