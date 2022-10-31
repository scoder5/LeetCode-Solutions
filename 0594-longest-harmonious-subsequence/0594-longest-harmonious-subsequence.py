class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        
        nums.sort()
        res = 0
        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            if nums[r] - nums[l] == 0:
                r += 1
            elif nums[r] - nums[l] == 1:
                res = max(res, r-l+1)
                r += 1
            else:
                l += 1
        return res
            