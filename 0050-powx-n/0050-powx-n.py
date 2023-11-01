class Solution:
    def myPower(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        tmp = self.myPow(x, n//2)
        if n % 2 == 0: 
            return tmp * tmp
        else:
            return x * tmp * tmp
    def myPow(self, x: float, n: int) -> float:
        res = self.myPower(x,abs(n))
        if n < 0:
            return 1/res
        else:
            return res