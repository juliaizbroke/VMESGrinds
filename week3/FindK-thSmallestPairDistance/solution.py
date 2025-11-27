
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        smallest_list = []
        for i in range (len(nums)-1):
            for j in range (i+1, len(nums)):
                smallest_list.append(abs(nums[i]-nums[j]))
        smallest_list.sort()
        return smallest_list[k-1]


# Example usage:
sol = Solution()
print(sol.smallestDistancePair([1,3,1], 1))  # Output: 0
print(sol.smallestDistancePair([1,6,1], 3))  # Output: 5
print(sol.smallestDistancePair([1,1,1], 2))  # Output: 0