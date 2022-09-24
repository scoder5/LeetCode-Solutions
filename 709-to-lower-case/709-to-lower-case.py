class Solution:
    def toLowerCase(self, s: str) -> str:
        arr = []
        for i in s:
            if 65 <= ord(i) <= 90:
                arr.append(chr(ord(i) + 32))
            else:
                arr.append(i)
        return ''.join(arr)