class Solution:
    def isValid(self, s: str) -> bool:
        check = {')':'(','}':'{',']':'['}
        stack = []

        for ch in s:
            if ch in check:
                if len(stack) == 0 or stack.pop() != check[ch]:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0
    
sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
print(sol.isValid("([)]"))
