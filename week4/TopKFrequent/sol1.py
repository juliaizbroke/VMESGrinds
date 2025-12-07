class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        minHeap = []
        for n, c in count.items():
            heapq.heappush(minHeap, [c, n])

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
