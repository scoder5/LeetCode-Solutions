class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = s.split(' ')
        res = []
        for i in range(len(arr)):
            if arr[i].isnumeric():
                res.append(int(arr[i]))
        return all(i < j for i, j in zip(res, res[1:]))