class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def remove_point(a, b):
            points.discard((a, b))
            for y in xdic[a]:
                if (a, y) in points:
                    remove_point(a, y)
                    
            for x in ydic[b]:
                if (x, b) in points:
                    remove_point(x, b)
                    
        xdic = defaultdict(list)
        ydic = defaultdict(list)
        points = {(i, j) for i, j in stones}
        
        for i, j in stones:
            xdic[i].append(j)
            ydic[j].append(i)
            
        count = 0
        for a, b in stones:
            if (a, b) in points:
                remove_point(a, b)
                count += 1
        return len(stones) - count