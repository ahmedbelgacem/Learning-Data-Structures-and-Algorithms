class Solution:
    def RLE(self, s: str):
        last = s[0]
        i = 1
        res = ""
        if len(s) == 1:
            return str(i) + last
        else:
            for c in s[1:]:
                if c == last:
                    i += 1
                else:
                    res += str(i) + last
                    last = c
                    i = 1
            res += str(i) + last
            return res

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.RLE(self.countAndSay(n - 1))
