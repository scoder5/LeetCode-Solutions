class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        data = Counter(changed)
        result = []
        for i in sorted(data):
            if data[i] < 0:
                return []
            val = i * 2
            while data[i] > 0:
                if val not in data and data[val] == 0 or i == 0 and data[i] < 2:
                    return []
                result.append(i)
                data[i] -= 1
                data[val] -= 1
                
        return result
        