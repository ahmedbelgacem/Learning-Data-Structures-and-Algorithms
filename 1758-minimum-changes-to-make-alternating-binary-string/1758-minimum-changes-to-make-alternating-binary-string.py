class Solution:
    def minOperations(self, s: str) -> int:
        count, el = 0, 0
        for i in range(len(s)):
            count += (s[i] == str(el))
            el = abs(1 - el)
        return min(count, len(s) - count)