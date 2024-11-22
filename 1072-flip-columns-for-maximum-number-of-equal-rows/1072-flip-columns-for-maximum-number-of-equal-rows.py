from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dic = defaultdict(int)
        for row in matrix:
            reverse = [1 - n for n in row]
            dic[str(row)] += 1
            dic[str(reverse)] += 1
        return max(dic.values())
