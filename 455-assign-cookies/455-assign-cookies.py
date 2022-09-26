class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l, r = 0, 0
        for c in s:
            if l >= len(g):
                return l
            if c >= g[l]:
                l += 1
        return l
            