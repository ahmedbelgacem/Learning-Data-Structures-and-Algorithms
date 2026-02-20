class Solution:
    def checkgrid(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    return False
        return True
    def backtrack(self, row: int, col: int):
        old = self.grid[row][col]
        if old == 2:
            if self.checkgrid():
                return 1
            else:
                return 0
        self.grid[row][col] = 1
        count = 0
        if col > 0:
            if self.grid[row][col - 1]==0 or self.grid[row][col - 1]==2:
                count+= self.backtrack(row, col - 1)
        if col < self.n - 1:
            if self.grid[row][col + 1]==0 or self.grid[row][col + 1]==2:
                count+= self.backtrack(row, col + 1)
        if row < self.m - 1:
            if self.grid[row + 1][col]==0 or self.grid[row + 1][col]==2:
                count+= self.backtrack(row + 1, col)
        if row > 0:
            if self.grid[row - 1][col]==0 or self.grid[row - 1][col]==2:
                count+= self.backtrack(row - 1, col)
        self.grid[row][col] = old
        return count
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    return self.backtrack(i,j)