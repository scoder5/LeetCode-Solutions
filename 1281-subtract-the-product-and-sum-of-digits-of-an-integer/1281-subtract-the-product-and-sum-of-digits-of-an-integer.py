class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = [int(i) for i in str(n)]
        p = 1
        for i in range(len(arr)):
            p *= arr[i]
        return p - sum(arr)