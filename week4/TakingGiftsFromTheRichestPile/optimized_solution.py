import heapq
import math

class Solution:
    def pickGifts(self, gifts, k: int) -> int:
        negative = [-g for g in gifts]
        heapq.heapify(negative)

        for i in range(k):
            largest = -1 * heapq.heappop(negative)
            reduced = int(math.isqrt(largest))
            heapq.heappush(negative, -1 * reduced)

        return -1 * sum(negative)