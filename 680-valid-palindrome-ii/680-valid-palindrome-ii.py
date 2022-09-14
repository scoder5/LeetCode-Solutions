class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            a = list(s)
            l, r = 0, len(a) - 1
            while l < r:
                if a[l] == a[r]:
                    l += 1
                    r -= 1
                elif a[l+1:r+1] == a[l+1:r+1][::-1]:
                    return True
                elif a[l:r] == a[l:r][::-1]:
                    return True
                else:
                    return False