class Solution:
    def countAsterisks(self, s: str) -> int:
        count, temp = 0, 0
        for i in range(len(s)):
            if s[i] == "|":
                temp += 1
            if s[i] == "*" and temp % 2 == 0:
                count += 1
        return count