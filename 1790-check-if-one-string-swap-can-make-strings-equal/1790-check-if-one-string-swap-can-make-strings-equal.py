class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s = 0
        l1 = list(s1)
        l1.sort()
        l2 = list(s2)
        l2.sort()
        if l1 != l2:
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                s += 1
        return s == 2 or s == 0