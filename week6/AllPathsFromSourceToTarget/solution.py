class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        n = len(graph)

        def dfs(node, path):
            if node == n - 1:
                res.append(path[:])
                return

            for nei in graph[node]:
                dfs(nei, path + [nei])

        dfs(0, [0])
        return res

sol = Solution()
print(sol.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))