class Solution:
    def placeable(self, row, col):
        res = True
        for i in range(0, self.n):
            for j in range(0, self.n):
                res = res and self.grid[i][col] != 1 and self.grid[row][j] != 1
                if i - j == row - col or i + j == row + col:
                    res = res and self.grid[i][j] != 1
        return res
    def place(self, row, col):
        self.grid[row][col] = 1
    def remove(self, row, col):
        self.grid[row][col] = 0
    def backtrack(self, row: int = 0, count: int = 0):
        for col in range(self.n):
            if self.placeable(row, col):
                self.place(row, col)
                if row + 1 == self.n:
                    count+=1
                else:
                    count = self.backtrack(row + 1, count)
                self.remove(row, col)
        return count
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.grid = [[0] * self.n for _ in range(self.n)]
        return self.backtrack(0, 0)
    