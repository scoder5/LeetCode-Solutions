class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            flag = 1
            idx = nums2.index(i)
            for j in range(idx+1, len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    flag = 0
                    break
                else:
                    flag = 1
                    continue
            if flag == 1:
                res.append(-1)
        return res