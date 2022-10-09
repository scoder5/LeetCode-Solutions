class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(b) // len(a)
        if b in a * n:
            return n
        if b in a * (n + 1):
            return n + 1
        if b in a * (n + 2):
            return n + 2
        return -1