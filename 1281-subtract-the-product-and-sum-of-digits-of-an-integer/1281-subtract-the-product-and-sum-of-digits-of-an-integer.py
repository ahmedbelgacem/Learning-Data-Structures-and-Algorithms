class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while n / 10 != 0 :
            s += n % 10
            p *= n % 10
            n = n // 10
        return p-s