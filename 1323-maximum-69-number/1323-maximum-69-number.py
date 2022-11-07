class Solution:
    def maximum69Number (self, num: int) -> int:
        arr = list(str(num))
        for i, j in enumerate(arr):
            if j == '6':
                arr[i] = '9'
                break
        return int("".join(arr))
            