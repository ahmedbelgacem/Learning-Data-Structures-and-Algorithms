class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        for i in range(n):
            if i not in visited:
                provinces += 1
                visited.add(i)
            queue = []
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    queue.append(j)
                    visited.add(j)
            while queue:
                j = queue.pop(0)
                for k in range(n):
                    if isConnected[j][k] == 1 and k not in visited:      
                        queue.append(k)
                        visited.add(k)
        return provinces