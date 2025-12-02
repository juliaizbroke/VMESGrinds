import heapq
from typing import List
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        count = 0
        max_amount = [-a for a in amount]
        heapq.heapify(max_amount)
        highest_amount = heapq.heappop(max_amount)
        while  -highest_amount > 0:
            second_highest = heapq.heappop(max_amount)
            if(-second_highest >0):
                highest_amount += 1
                second_highest += 1
            else:
                highest_amount += 1

            heapq.heappush(max_amount, highest_amount)
            heapq.heappush(max_amount, second_highest)
            highest_amount = heapq.heappop(max_amount)
            count += 1
        return count
    
# Example usage:
sol = Solution()
print(sol.fillCups([1,4,2]))  # Output: 4
print(sol.fillCups([5,4,4]))  # Output: 7


             