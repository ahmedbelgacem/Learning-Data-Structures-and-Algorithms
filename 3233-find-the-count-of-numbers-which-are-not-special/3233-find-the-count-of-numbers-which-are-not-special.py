class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        lim = int(math.sqrt(r))
        prime = [True] * (lim + 1)
        prime[0] = prime[1] = False
        for i in range(2, int(math.sqrt(lim)) + 1):
            if prime[i]:
                for j in range(i*i, lim + 1, i):
                    prime[j] = False
        count = 0
        for i in range(2, lim + 1):
            if prime[i]:
                if i*i in range(l, r + 1):
                    count += 1
        return r - l + 1 - count