class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
        counts = collections.Counter(even)
        if len(even) > 0:
            return max(counts, key = counts.get)
        else:
            return -1