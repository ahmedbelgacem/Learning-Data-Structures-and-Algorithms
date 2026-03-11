class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if not n else (2 ** math.floor(math.log2(n) + 1) - 1 - n)