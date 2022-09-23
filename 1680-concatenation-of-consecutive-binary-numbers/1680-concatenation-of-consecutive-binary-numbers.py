class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = []
        for i in range(1, n+1):
            res.append(bin(i).replace("0b", ""))
        
        a = "".join(res)
        return int(a, 2) % (10 ** 9 + 7)