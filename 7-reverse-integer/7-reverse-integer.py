class Solution:
    def reverse(self, x: int) -> int:
        res = -1 * int(str(-1 * x)[::-1]) if x < 0 else int(str(x)[::-1])
        return res if res > -2**31 and res < 2**31 - 1 else 0