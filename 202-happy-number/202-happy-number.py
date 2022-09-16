class Solution:
    def isHappy(self, n: int) -> bool:
        while len(str(n)) != 1:
            array = [int(i) ** 2 for i in str(n)]
            n = sum(array)
            
        if n == 1 or n == 7:
            return True
        