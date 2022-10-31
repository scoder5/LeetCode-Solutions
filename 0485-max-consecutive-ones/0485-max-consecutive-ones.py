class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, maxc = 0, 0
        for i in nums:
            if i == 1:
                count += 1
                maxc = max(maxc, count)
            else:
                count = 0
        return maxc
                