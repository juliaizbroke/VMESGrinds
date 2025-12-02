from typing import List
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        count = 0
        while amount[0] > 0:
            if(amount[1]>0):
                amount[1] -= 1
                amount[0] -= 1
            else:
                amount[0] -= 1

            count += 1
            amount.sort(reverse = True)
        return count

# Example usage:
sol = Solution()
print(sol.fillCups([1,4,2]))  # Output: 4
print(sol.fillCups([5,4,4]))  # Output: 7
