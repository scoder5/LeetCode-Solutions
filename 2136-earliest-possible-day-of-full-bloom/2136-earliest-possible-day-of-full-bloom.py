class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        res = 0 
        for g, p in sorted(zip(growTime, plantTime)):
            res = g + p if g >= res else res + p
        return res