class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([i for i in f"{n:b}" if i == "1"])