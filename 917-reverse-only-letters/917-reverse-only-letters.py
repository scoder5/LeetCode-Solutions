class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        l, r = 0, len(arr) - 1
        special = "`~!@#$%^&*()-_=+{}[]:;'<>,.?/\|"
        while l < r:
            while l < r and not(arr[l].isalpha()):
                l += 1
            while l < r and not(arr[r].isalpha()):
                r -= 1
                
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
                
        return ''.join(arr)