import heapq
class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        if multiplier == 1:
            return nums

        n = len(nums)
        maxVal = max(nums)

        minH = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(minH)

        while 0 < k:
            x, i = minH[0]
            newX = x * multiplier
            if newX > maxVal:
                break
            heapq.heappop(minH)
            heapq.heappush(minH, (newX, i))
            k -= 1

        exp = k // n
        rem = k % n

        m = 10**9+7

        extra = pow(multiplier,exp+1,m)
        normal = pow(multiplier,exp,m)

        res = [0] * n

        for j in range(n):
            x, i = heapq.heappop(minH)
            if j < rem:
                res[i] = (x % m * extra) % m
            else:
                res[i] = (x % m * normal) % m

        return res
    
sol = Solution()
print(sol.getFinalState([2,1,3,5,6],5,2))
print(sol.getFinalState([100000,2000],2,1000000))
print(sol.getFinalState([161209470],56851412,39846))