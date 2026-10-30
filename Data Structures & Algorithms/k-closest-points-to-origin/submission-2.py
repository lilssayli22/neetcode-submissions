import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x*x + y*y, x, y) for x, y in points]
        heapq.heapify(heap)                      # O(n)
        return [[x, y] for _, x, y in (heapq.heappop(heap) for _ in range(k))]  # O(k log n)