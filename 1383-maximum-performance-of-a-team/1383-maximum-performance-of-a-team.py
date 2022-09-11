class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        curSum, h = 0 ,[]
        ans = -float('inf')
        for i, j in sorted(zip(efficiency, speed), reverse = True):
            while len(h) > k-1:
                curSum -= heappop(h)
            heappush(h, j)
            curSum += j
            ans = max(ans, curSum * i)
            
        return ans % (10 ** 9+7)