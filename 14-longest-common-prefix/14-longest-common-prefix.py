class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        smallest = strs[0]
        for word in strs:
            if len(word) < len(smallest):
                smallest = word
        for idx, char in enumerate(smallest):
            for word in strs:
                if word[idx] != char:
                    return smallest[:idx]
        return smallest
