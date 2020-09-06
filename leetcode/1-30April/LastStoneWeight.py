import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for x in stones:
            heap.append(-x)

        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x < y:
                newStone = (-x) - (-y)
                heapq.heappush(heap, -newStone)

        if len(heap) == 0:
            return 0
        else:
            return -heapq.heappop(heap)
