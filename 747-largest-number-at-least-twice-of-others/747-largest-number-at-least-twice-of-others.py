class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) ==  1:
            return 0
        large = max(nums)
        if large >= 2 * sorted(nums)[-2]:
            return nums.index(large)
        return -1