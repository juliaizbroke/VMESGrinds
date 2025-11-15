class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            new_n = 0
            while n > 0:
                new_n += (n%10)**2
                n = n//10
            if(new_n in seen):
                return False
            n = new_n
            seen.add(n)
        return True
        
# Example usage:
sol = Solution()
print(sol.isHappy(19))  # Output: True
print(sol.isHappy(2))   # Output: False