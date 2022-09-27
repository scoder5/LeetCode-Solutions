class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(n):
            res = 0
            while n != 0:
                res += n%2
                n //= 2
            return res
        counts = []
        for i in arr:
            counts.append(countBits(i))
        return [j for i, j in sorted(zip(counts, arr))]
        
            