class BounceCounter:
    def __init__(self, n: int):
        self.n = n
        self.i = 0
        self.direction = 1 
    def next(self) -> int:
        value = self.i
        if self.i == self.n:
            self.direction = -1
        elif self.i == 0:
            self.direction = 1
        self.i += self.direction
        return value

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        bounce = BounceCounter(numRows - 1)
        result = ""
        for c in s:
            rows[bounce.next()] += c
        return "".join(rows)
