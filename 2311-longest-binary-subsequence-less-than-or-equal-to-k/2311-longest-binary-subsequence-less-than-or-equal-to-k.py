class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        if int(s, 2) <= k:
            return len(s)
        else:
            s = s.replace('1','', 1)
            return self.longestSubsequence(s, k)