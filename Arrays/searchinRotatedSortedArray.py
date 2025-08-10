class Solution:
    def getPivot(self, nums : List[int], low: int, high: int):
        while(low < high):
            mid  = low +(high - low)//2
            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid+1
        return low
    
    def binarySearch(self, nums: List[int], low: int, high: int, target: int):
        while low<=high:
            mid = low + (high -low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1


    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = self.getPivot(nums, 0, n-1)
        if(nums[pivot] <=target):
            return self.binarySearch(nums, pivot, n-1, target)
        else:
            return self.binarySearch(nums, 0, pivot-1, target)
        
