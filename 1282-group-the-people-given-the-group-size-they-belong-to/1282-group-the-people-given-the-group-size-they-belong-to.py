from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        res = []
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
        for size in d.keys():
            for i in range(0, len(d[size]), size):
                res.append(d[size][i: i + size])
        return res