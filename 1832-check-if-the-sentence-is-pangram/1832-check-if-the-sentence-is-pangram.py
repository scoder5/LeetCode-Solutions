class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(26):
            char = chr(ord('a') + i)
            if sentence.find(char) == -1:
                return False
        return True