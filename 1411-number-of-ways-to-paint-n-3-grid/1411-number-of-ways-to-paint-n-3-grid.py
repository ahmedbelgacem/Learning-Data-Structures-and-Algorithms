class Solution:
    def numOfWays(self, n: int) -> int:
        n_different = 6
        n_alternate = 6
        i = 1
        while i < n:
            n_different, n_alternate =  n_different * 2 + n_alternate * 2, n_different * 2 + n_alternate * 3
            i+=1
        return (n_different + n_alternate) % (10**9 + 7)