
from ast import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if(token == '+'):
                    stack.append(a+b)
                elif(token == '-'):
                    stack.append(a-b)
                elif(token == '*'):
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))

        return stack.pop()
    

# Example usage:
sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
print(sol.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6
print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # Output: 22