class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        hset = set()
        for i in range(len(nums) - 1):
            sums = nums[i] + nums[i+1]
            if sums in hset:
                return True
            else:
                hset.add(sums)
                
        return False