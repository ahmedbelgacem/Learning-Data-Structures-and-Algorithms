class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        l = [int(s[0]), int(s[1]), int(s[2]), int(s[3])]
        l.sort()
        return (l[0]*10 + l[2]) + (l[1]*10 + l[3])