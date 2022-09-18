class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        l, r = 0, 0
        while l < m and r < n:
            if s[l] == t[r]:
                l += 1
            r += 1
        return l == m