class Solution(object):
    def findJudge(self, n, trust):
        if n == 1:
            return 1

        # build adjacency list (who each person trusts)
        graph = [[] for _ in range(n + 1)]
        for a, b in trust:
            graph[a].append(b)

        # check each person as potential judge
        for candidate in range(1, n + 1):
            # condition 1: judge trusts nobody
            if graph[candidate]:
                continue

            trusted_by_all = True
            for other in range(1, n + 1):
                if other == candidate:
                    continue
                if candidate not in graph[other]:
                    trusted_by_all = False
                    break

            if trusted_by_all:
                return candidate

        return -1
