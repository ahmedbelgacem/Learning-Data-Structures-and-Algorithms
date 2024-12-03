class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        idx = 0
        res = ""
        for space in spaces:
            res += s[idx:space]
            res += " "
            idx = space
        res += s[space:]
        return res
