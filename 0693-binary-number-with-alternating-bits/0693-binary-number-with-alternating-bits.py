class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = format(n, 'b')
        last = n[0]
        for i in range(1, len(n)):
            if n[i] == last:
                return False
            else:
                last = n[i]
        return True