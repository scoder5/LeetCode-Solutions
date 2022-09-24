class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == magazine:
            return True
        r, m = sorted(list(ransomNote)), sorted(list(magazine))
        for i in m:
            if r and i in r[0]:
                r.pop(0)
                
        return False if r else True
        