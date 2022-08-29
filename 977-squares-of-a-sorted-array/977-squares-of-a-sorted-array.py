class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = [i ** 2 for i in sorted(nums)]
        return sorted(l)