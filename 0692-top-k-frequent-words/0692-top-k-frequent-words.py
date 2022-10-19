class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return list(zip(*collections.Counter(sorted(words)).most_common(k)))[0]