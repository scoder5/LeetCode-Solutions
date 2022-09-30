class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        tombstones = {}
        def heap_remove(heap, value):
            tombstones[value] = tombstones.get(value, 0) + 1
            while len(heap) and heap[0] in tombstones and tombstones[heap[0]]:
                tombstones[heap[0]] = tombstones.get(heap[0]) - 1
                heappop(heap)
            return heap
        points = []
        for Li, Ri, Hi in buildings:
            points.append((Li, -Hi, 1))
            points.append((Ri, Hi, -1)                                                                                                                                                                      )
        points.sort()
        pq, max_height = [0], 0
        key_points = []
        for x, h, s in points:
            if s == 1: # start point
                if -h > max_height:
                    max_height = -h
                    key_points.append([x, -h])
                heapq.heappush(pq,h)
            else: # end point
                pq = heap_remove(pq,-h)
                pq_max = -pq[0]
                if pq_max < max_height:
                    max_height = pq_max
                    key_points.append([x, max_height])
        return key_points