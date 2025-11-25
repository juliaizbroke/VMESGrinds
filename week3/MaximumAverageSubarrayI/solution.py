class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_s = float("-inf")
        for i in range(len(nums)-k+1):
            cur_s = sum(nums[i:i+k])
            max_s = max(max_s, cur_s)
        return max_s / k
