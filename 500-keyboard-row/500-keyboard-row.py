class Solution:
    def findWords(self, words: List[str]) -> List[str]:
            val1 = sorted("qwertyuiop")
            val2 = sorted("asdfghjkl")
            val3 = sorted("zxcvbnm")
            keyboard = {1:val1, 2:val2, 3:val3}
            res = []

            for word in words:
                if  all(item in keyboard[1] for item in sorted(word.lower())):
                    res.append(word)
                elif all(item in keyboard[2] for item in sorted(word.lower())):
                    res.append(word)
                elif all(item in keyboard[3] for item in sorted(word.lower())):
                    res.append(word)
            return res