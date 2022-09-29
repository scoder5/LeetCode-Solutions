class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(nums, target, lb):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                m = (l + r) // 2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m-1
                else:
                    i = m
                    if lb:
                        r = m - 1 
                    else:
                        l = m + 1
                    
            return i
        left = binSearch(nums, target, True)
        right = binSearch(nums, target, False)
        return [left, right]