import heapq


class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        maxHeap = []
        for num, freq in count.items():
            heapq.heappush(maxHeap, (-freq, num))

        result = []
        for _ in range(k):
            freq, num = heapq.heappop(maxHeap)
            result.append(num)

        return result
