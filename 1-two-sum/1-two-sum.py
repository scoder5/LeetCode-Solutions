class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hmap:
                return [hmap[dif], i]
            hmap[n] = i
        return