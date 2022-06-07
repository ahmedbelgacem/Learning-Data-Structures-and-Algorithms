class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 for stone in list(stones) if stone in jewels])