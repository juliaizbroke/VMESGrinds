class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        left = 1000
        right = -1000
        res = 0

        for i in range(len(nums)):
            if nums[i] <= threshold:
                if left == 1000 and nums[i] % 2 == 0:
                    left = i
                    right = i
                if i < len(nums)-1 and nums[i+1] <= threshold and nums[i] % 2 != nums[i+1] % 2:
                    right = i+1
                else:
                    res = max(res,i-left+1)
                    left = 1000
                    right = -1000
                res = max(res,right-left+1)
            else:
                left = 1000
                right = -1000
        
        return res
    
sol = Solution()
print(sol.longestAlternatingSubarray([3,2,5,4], 5))
print(sol.longestAlternatingSubarray([1,2], 2))
print(sol.longestAlternatingSubarray([2,3,4,5], 4))