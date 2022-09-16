import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        for i in sorted(counts):
            if counts[i] == 1:
                return i
            
        