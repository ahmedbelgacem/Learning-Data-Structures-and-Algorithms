class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        seen_chars = set()
        for right in range(len(s)):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            seen_chars.add(s[right])
            length = max(length, right - left + 1)
        return length
             