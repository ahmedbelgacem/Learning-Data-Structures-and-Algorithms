class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        i = 0
        sign = 1
        while i < len(s):
            if s[i] == " ":
                i += 1
            else:
                if s[i] == "-":
                    sign = -1
                    i += 1
                elif s[i] == "+":
                    i += 1
                break
        while i < len(s):
            if not s[i].isdigit():
                break
            else:
                res = res * 10 + int(s[i])
                i += 1
        if res >= pow(2, 31) - 1:
            if res > pow(2, 31) - 1 and sign == -1:
                res = pow(2, 31)
            else:
                res = pow(2, 31) - 1
        return res * sign
