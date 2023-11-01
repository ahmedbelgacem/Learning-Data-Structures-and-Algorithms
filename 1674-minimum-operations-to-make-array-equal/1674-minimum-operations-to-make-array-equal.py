class Solution:
    def minOperations(self, n: int) -> int:
        s = 0
        for i in range(n):
            if (2 * i + 1) < n:
                s+=n-(2 * i + 1)
            else:
                break
        return s