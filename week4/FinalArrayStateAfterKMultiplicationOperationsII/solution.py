import heapq
class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        n = len(nums)
        minH = []
        res = [0] * n

        for i, val in enumerate(nums):
            heapq.heappush(minH, (val,i))

        for i in range(k):
            x, i = heapq.heappop(minH)
            newX = x * multiplier
            heapq.heappush(minH, (newX, i))

        for j in range(n):
            x, i = heapq.heappop(minH)
            res[i] = x % (10**9+7)

        return res
    
sol = Solution()
print(sol.getFinalState([2,1,3,5,6],5,2))
print(sol.getFinalState([100000,2000],2,1000000))
print(sol.getFinalState([161209470],56851412,39846))