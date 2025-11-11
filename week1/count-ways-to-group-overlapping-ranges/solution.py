class Solution(object):
    def countWays(self, ranges):
        MOD = 10**9 + 7
        ranges.sort()

        groups = 0

        i = 0
        n = len(ranges)
        while i < n:
            groups += 1
            end = ranges[i][1]
            i += 1
            while i < n and ranges[i][0] <= end:
                end = max(end, ranges[i][1])
                i += 1

        return pow(2, groups, MOD)


# 31ms
