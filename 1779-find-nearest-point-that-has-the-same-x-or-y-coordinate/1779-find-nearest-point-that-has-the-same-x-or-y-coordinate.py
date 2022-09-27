class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mind = math.inf
        ans = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                mand = abs(points[i][0] - x) + abs(points[i][1] - y)
                if mand < mind:
                    ans = i
                    mind = mand
        return ans