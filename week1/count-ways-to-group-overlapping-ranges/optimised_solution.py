class Solution:
    def countWays(self, ranges):
        MOD = 10**9 + 7
        ranges.sort()
        groups = 0
        end = -1

        for start, finish in ranges:
            if start > end:
                groups += 1
                end = finish
            else:
                end = max(end, finish)

        return pow(2, groups, MOD)
# 19ms
