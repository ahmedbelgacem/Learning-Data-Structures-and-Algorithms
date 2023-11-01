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
            for idx, adj in enumerate(isConnected[i]):
                if adj and idx not in visited:
                    queue.append(idx)
                    visited.add(idx)
            while queue:
                j = queue.pop(0)
                for idx, adj in enumerate(isConnected[j]):
                    if adj and idx not in visited:
                        queue.append(idx)
                        visited.add(idx)
        return provinces
