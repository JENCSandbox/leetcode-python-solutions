# https://leetcode.com/problems/k-closest-points-to-origin/description/
# https://www.youtube.com/watch?v=rI2EBUEMfTk
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist,x,y])

        heapq.heapify(minHeap)
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1

        return res


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        points = sorted(points, key = lambda points: points[0] * points[0] + points[1] * points[1])
        return points[:k]