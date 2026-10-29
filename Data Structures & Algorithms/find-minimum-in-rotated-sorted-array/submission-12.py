class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if len(nums) == 1:
            return nums[0]

        while start < end:
            mid = (start + end)//2
            print(nums[mid])
            if nums[mid - 1] > nums[mid] and len(nums):
                return nums[mid]
            if nums[mid + 1] < nums[mid] and len(nums) == 2:
                return nums[mid + 1]
            
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
