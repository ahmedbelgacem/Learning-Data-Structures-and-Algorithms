class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        idx = 0
        last = 0
        res = ""
        for space in spaces:
            while idx < space:
                idx += 1
            res += s[last:idx]
            res += " "
            last = idx
        res += s[last:]
        return res
