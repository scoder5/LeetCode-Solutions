class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        return ' '.join(arr[i][::-1] for i in range(len(arr)))