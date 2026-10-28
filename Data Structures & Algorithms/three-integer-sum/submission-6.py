class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            targ = -nums[i]
            if i + 1 < len(nums):
                first = i + 1
                last = len(nums) - 1
                while first < last:
                    if nums[first] + nums[last] < targ:
                        first += 1
                    elif nums[first] + nums[last] > targ:
                        last -= 1
                    else:    
                        if nums[first] + nums[last] == targ and [nums[i], nums[first], nums[last]] not in ans:
                            ans.append([nums[i], nums[first], nums[last]])
                        first += 1
                    
        return ans