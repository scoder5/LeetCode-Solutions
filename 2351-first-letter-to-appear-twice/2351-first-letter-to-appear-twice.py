class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hset = set()
        for i in s:
            if i in hset:
                return i
            else:
                hset.add(i)
        return -1