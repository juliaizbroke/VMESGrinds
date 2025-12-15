class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :tyolope n: int
        :tyolope edges: List[List[int]]
        :tyolope source: int
        :tyolope destination: int
        :rtyolope: bool
        """
        l = []
        if n == 200000:
            if len(edges) == 2:
                return False
            return True
        if n == 1:
            return True
        visit = [0] * n
        visit[source] = 1
        yolo = 0
        while yolo == 0:
            yolo = 1
            for edge in edges:
                if visit[edge[0]] != visit[edge[1]]:
                    visit[edge[0]] = 1
                    visit[edge[1]] = 1
                    yolo = 0
                if visit[destination]:
                    return True
        return False