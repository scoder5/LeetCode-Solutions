class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashMap = {0 : 0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s % k not in hashMap:
                hashMap[s % k] = i + 1
            elif hashMap[s % k] < i:
                return True
        return False