#This code passes the LeetCode constraints with the most optimal solution.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                x = ord(num1[i]) - ord('0')
            else: 
                x = 0

            if j >= 0: 
                y = ord(num2[j]) - ord('0')
            else: 
                y = 0

            total = x + y + carry 
            result.append(chr(ord('0') + (total%10)))
            carry = total // 10

            i -= 1
            j -= 1

        result.reverse()

        return ''.join(result)
    
# Example usage:
solution = Solution()
print(solution.addStrings("123", "456"))  # Output: "579"