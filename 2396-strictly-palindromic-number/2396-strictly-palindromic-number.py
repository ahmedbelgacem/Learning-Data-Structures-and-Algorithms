class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base(n, base):
            digits = []
            while n:
                digits.append(str(n % base))
                n //= base
            return ''.join(reversed(digits))
        for i in range(2, n - 1):
            s = to_base(n, i)
            if s != s[::-1]:
                return False
        return True