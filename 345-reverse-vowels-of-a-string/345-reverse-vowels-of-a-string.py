class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        a = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if a[l] not in vowels:
                l += 1
            elif a[r] not in vowels:
                r -= 1
            else:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1
        
        return ''.join(a)