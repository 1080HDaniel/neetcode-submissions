class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        john = set(nums)
        left = int()
        cons = 0
        if not nums:
            return 0
        
        for i in nums:
            if i - 1 not in john:
                left = i
                temp = 1
                while left + 1 in john:
                    temp += 1
                    left += 1
                cons = max(cons, temp)
                

        return cons
        