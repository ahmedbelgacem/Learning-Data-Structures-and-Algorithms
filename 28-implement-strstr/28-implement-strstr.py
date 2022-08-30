class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        current = 0
        c = needle[0]
        idx = 0
        while idx < len(haystack):
            char = haystack[idx]
            if char == c:
                if current == len(needle) - 1:
                    return(idx - len(needle) + 1)
                current = current + 1
                c = needle[current]
            else:
                if current != 0:
                    idx = idx - current
                    current = 0
                    c = needle[0]
            idx = idx + 1
        return -1
            