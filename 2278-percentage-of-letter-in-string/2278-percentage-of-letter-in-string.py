class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        count = 0
        for i in range(len(s)):
            if s[i] == letter:
                count += 1
        return int((count / len(s)) * 100)