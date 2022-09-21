class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        dc = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dc += 1
            
        return True if dc <= 2 and sorted(s1) == sorted(s2) else False