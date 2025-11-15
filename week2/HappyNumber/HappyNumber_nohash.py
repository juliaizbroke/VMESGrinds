class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x):
            total = 0
            while x > 0:
                d = x % 10
                total += d * d
                x //= 10
            return total

        slow = n
        fast = get_next(n)
        # advance until fast reaches 1 (happy), or slow meets fast (cycle)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
    
# Example usage:
sol = Solution()
print(sol.isHappy(19))  # Output: True
print(sol.isHappy(2))   # Output: False
