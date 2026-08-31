class Solution:
    def minimumSum(self, num: int) -> int:
        l = sorted(str(num))
        return (int(l[0]) * 10 + int(l[2])) + (int(l[1])*10 + int(l[3]))