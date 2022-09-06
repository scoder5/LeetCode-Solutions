class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_ele = max(nums)
        min_ele = min(nums)
        
        if min_ele + k >= max_ele - k:
            return 0
        else:
            return (max_ele - k) - (min_ele + k)