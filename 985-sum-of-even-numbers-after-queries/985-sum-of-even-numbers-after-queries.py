class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(i for i in nums if i % 2 == 0)
        res = []
        for i, j in queries:
            if nums[j] % 2 == 0:
                s -= nums[j]
            nums[j] += i
            if nums[j] % 2 == 0:
                s += nums[j]
            res.append(s)
        return res
            