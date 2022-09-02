class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        res = sum(nums[l:l+k])
        ans = res
        for r in range(l+k, len(nums)):
            res -= nums[l]
            res += nums[r]
            ans = max(res, ans)
            l += 1
            
        return ans/k