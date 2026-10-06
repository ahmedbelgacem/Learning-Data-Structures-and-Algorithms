class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = s.count("1")
        return "1" * (n - 1) + "0" * (len(s) - n) + "1"




