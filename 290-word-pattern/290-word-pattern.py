class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        CTW, WTC = {}, {}
        for c, w in zip(pattern, words):
            if c in CTW and CTW[c] != w:
                return False
            if w in WTC and WTC[w] != c:
                return False
            CTW[c] = w
            WTC[w] = c
        return True