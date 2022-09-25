class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = []
        for i in range(len(sentences)):
            res.append(sentences[i].split())
        return max(len(res[i]) for i in range(len(res)))           