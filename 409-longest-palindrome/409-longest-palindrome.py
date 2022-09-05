class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        result, odd_found = 0, False
        for i,j in counts.items():
            if j%2 == 0:
                result += j
            else:
                odd_found = True
                result += j - 1
        if odd_found:
            result += 1
        return result