class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last = 0
        res = 0
        for row in bank:
            if row.count("1"):
                cur = row.count("1")
                res+= cur * last
                last = cur
        return res