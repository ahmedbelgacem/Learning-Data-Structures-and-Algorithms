from collections import defaultdict
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        d = defaultdict(list)
        for i in range(len(points)):
            x, y = points[i]
            val = max(abs(x), abs(y))
            d[val].append(s[i])
        l = list(d.keys())
        l.sort()
        res = 0
        last = []
        for val in l:
            tmp = last + d[val]
            if len(list(set(tmp))) == len(tmp):
                last = tmp
                res = len(tmp)
            else:
                break
        return res

