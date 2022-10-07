class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums
        else:
            odd, even = [], []
            for i in range(len(nums)):
                if i % 2 != 0:
                    odd.append(nums[i])
                else:
                    even.append(nums[i])
            odd.sort(reverse=True)
            even.sort()
            l, r = 0, 0
            for i in range(len(nums)):
                if i % 2 == 0:
                    nums[i] = even[l]
                    l += 1
                else:
                    nums[i] = odd[r]
                    r += 1
            return nums