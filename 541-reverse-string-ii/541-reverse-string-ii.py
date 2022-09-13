class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        for i in range(0,n,2*k):
            if i==0:
                s = self.rev(s[0:k])+s[k:]
            elif 0 < i < n:
                s = s[:i]+self.rev(s[i:i+k])+s[i+k:]
        return s

    def rev(self,s):
        return s[::-1]