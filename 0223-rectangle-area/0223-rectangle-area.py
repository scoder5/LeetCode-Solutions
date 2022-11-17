class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        aa = (ay2 - ay1) * (ax2 - ax1)
        ab = (by2 - by1) * (bx2 - bx1)
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        xo = right - left
        
        top = min(ay2, by2)
        bot = max(ay1, by1)
        yo = top - bot
        
        aro = 0
        if xo > 0 and yo > 0:
            aro = xo * yo
        total = aa + ab - aro
        return total