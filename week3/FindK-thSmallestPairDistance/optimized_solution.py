
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_pairs(max_dist):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > max_dist:
                    left += 1
                count += right - left
            return count

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if count_pairs(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

# Example usage:
sol = Solution()
print(sol.smallestDistancePair([1,3,1], 1))  # Output: 0
print(sol.smallestDistancePair([1,6,1], 3))  # Output: 5
print(sol.smallestDistancePair([1,1,1], 2))  # Output: 0