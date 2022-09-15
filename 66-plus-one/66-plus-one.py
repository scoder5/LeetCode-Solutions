class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])

        val = ''.join(digits)
        a = int(val) + 1
        return [int(i) for i in str(a)]