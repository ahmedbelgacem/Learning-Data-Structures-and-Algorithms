def maxColumn(L):
    return list(map(max, zip(*L)))

def maxRow(L):
    return list(map(max, L))
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        rm = maxRow(grid)
        cm = maxColumn(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += min(rm[i],cm[j]) - grid[i][j]
        return total