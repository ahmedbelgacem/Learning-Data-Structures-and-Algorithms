class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        curr = 0
        for l in s:
            if l == '(':
                curr += 1
            if l == ')':
                if curr > 0:
                    curr -= 1
                else:
                    res += 1
        res += curr
        return res