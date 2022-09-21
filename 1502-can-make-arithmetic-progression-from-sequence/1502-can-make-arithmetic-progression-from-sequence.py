class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[0] - arr[1]
        for i in range(2, len(arr)):
            if d != arr[i-1] - arr[i]:
                return False
        return True
    