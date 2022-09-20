class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == nums2:
            return len(nums1)
        count = 0
        dp = [[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1] 
                    count = max(count, dp[i][j])
                    
        return count
                    