class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = garbage[0].count('G') + garbage[0].count('M') + garbage[0].count('P')
        g, m, p = 0, 0, 0
        for i in range(1, len(garbage)):
            if garbage[i].count('G'):
                g = i
                res+= garbage[i].count('G')
            if garbage[i].count('M'):
                m = i
                res+= garbage[i].count('M')
            if garbage[i].count('P'):
                p = i
                res+= garbage[i].count('P')
        for i in range(g):
            res += travel[i]
        for i in range(m):
            res += travel[i]
        for i in range(p):
            res += travel[i]
        return res