class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        left = -1
        res = 0

        for i in range(len(nums)):
            if nums[i] > threshold:
                left = -1
                continue

            if left == -1:
                if nums[i] % 2 == 0:
                    left = i
                else:
                    continue

            if i + 1 < len(nums) and nums[i+1] <= threshold and (nums[i] % 2 != nums[i+1] % 2):
                res = max(res, i - left + 2)
            else:
                res = max(res, i - left + 1)
                left = -1

        return res
    
sol = Solution()
print(sol.longestAlternatingSubarray([3,2,5,4], 5))
print(sol.longestAlternatingSubarray([1,2], 2))
print(sol.longestAlternatingSubarray([2,3,4,5], 4))