class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        l = [0] * n
        count = 0
        for edge in edges:
            l[edge[1]] = 1
        for i in range(n):
            if not l[i]:
                count += 1
                res = i
        if count == 1:
            return res
        else:
            return -1
        
