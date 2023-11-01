class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        smallest = min(strs, key=len)
        for idx, char in enumerate(smallest):
            for word in strs:
                if word[idx] != char:
                    return smallest[:idx]
        return smallest
