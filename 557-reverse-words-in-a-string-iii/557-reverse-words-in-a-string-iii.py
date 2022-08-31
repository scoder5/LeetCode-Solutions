class Solution:
    def reverseWords(self, s: str) -> str:
        c = s.split()
        for i in range(len(c)):
            c[i] = c[i][::-1]
            
        return " ".join(c)