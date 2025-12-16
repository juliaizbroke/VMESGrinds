class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res = []
        sol = []
        n = len(graph)

        def dfs(node):
            sol.append(node)
            if node == n - 1:
                res.append(sol.copy())
            else:
                for nei in graph[node]:
                    dfs(nei)
            sol.pop()

        dfs(0)
        return res
    
sol = Solution()
print(sol.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))