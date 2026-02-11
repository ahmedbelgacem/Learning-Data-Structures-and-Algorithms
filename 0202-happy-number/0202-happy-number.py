class Solution:
    def sumSquares(self, n: int) -> int:
        s = str(n)
        res = 0
        for c in s:
            res+= int(c)**2
        return res

    def isHappy(self, n: int) -> bool:
        slow = self.sumSquares(n)
        fast = self.sumSquares(self.sumSquares(n))
        while slow != fast and fast != 1:
            slow = self.sumSquares(slow)
            fast = self.sumSquares(self.sumSquares(fast))
        return fast == 1
