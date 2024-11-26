class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        l = []
        res = 0
        for edge in edges:
            l.append(edge[1])
        for i in range(n):
            if i not in l:
                res += 1
                tmp = i
        if res == 1:
            return tmp
        else:
            return -1
        
