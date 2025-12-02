class Solution(object):
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)

        cache = {}
        for t in tasks:
            cache[t] = cache.get(t, 0) + 1

        maxf = max(cache.values())
        k = sum(1 for v in cache.values() if v == maxf)

        return max(len(tasks), (maxf - 1) * (n + 1) + k)