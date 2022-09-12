class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        curScore, maxScore = 0, 0
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                curScore += 1
                l += 1
                maxScore = max(maxScore, curScore)
            elif curScore > 0:
                power += tokens[r]
                curScore -= 1
                r -= 1
                maxScore = max(maxScore, curScore)
            else:
                break
                
        return maxScore