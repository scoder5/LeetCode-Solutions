from math import sqrt

class Solution:
    def bulbSwitch(self, n: int) -> int:
        if not n:
            return 0
        if n == 1:
            return 1
        return int(sqrt(n))
            