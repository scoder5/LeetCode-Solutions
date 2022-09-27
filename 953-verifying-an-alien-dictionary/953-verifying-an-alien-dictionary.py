class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {}
        for i, n in enumerate(order):
            hmap[n] = i
            
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if hmap[words[i][j]] > hmap[words[i+1][j]]:
                        return False
                    break
        return True