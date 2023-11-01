class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        i, s = 0, 0
        while i < n:
            s += piles[len(piles)-2 - 2*i]
            i = i+1            
        return s