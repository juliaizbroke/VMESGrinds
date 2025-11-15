## This code passes the LeetCode constraints but takes more time than the optimal solution.
class Solution:

    def addStrings(self, num1: str, num2: str) -> str:

        def str_to_int (s: str) -> int:
            num = 0
            for ch in s:
                num = num * 10 + (ord(ch) - ord('0'))
            return num

        def int_to_str (num: int) -> str:
            if num == 0:
                return '0'
            digits = []
            while num > 0:
                digit = num % 10
                digits.append(chr(ord('0') + digit))
                num = num // 10
            digits.reverse()
            result = ''.join(digits)
            return result

        num1_int = str_to_int(num1)
        num2_int = str_to_int(num2)
        
        ans_int = num1_int + num2_int
        ans_str = int_to_str(ans_int)
        return ans_str
    
# Example usage:
solution = Solution()
print(solution.addStrings("123", "456"))  # Output: "579"   