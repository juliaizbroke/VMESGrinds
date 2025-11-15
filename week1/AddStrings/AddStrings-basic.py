## This will not pass the LeetCode constraints but is a straightforward implementation.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_int = int(num1)
        num2_int = int(num2)
        ans_int = num1_int + num2_int
        ans_str = str(ans_int)
        return ans_str
    
# Example usage:
solution = Solution()
print(solution.addStrings("123", "456"))  # Output: "579"