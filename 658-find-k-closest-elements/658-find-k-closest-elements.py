class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = k, len(arr)
        while l < r:
            m = (l + r) // 2
            a, b = arr[m], arr[m-k]
            if a-x >= x-b:
                r = m
            else:
                l = m + 1
        return arr[l-k:r]