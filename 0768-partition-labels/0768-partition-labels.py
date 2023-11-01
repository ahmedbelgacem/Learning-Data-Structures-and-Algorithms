class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        tmp = [s[0]]
        for i in range(1, len(s)):
            exist = False
            for l in tmp:
                if l in s[i:]:
                    exist = True
                    tmp.append(s[i])
                    break
            if not exist:
                res.append(len(tmp))
                tmp = [s[i]]
        if tmp:
            res.append(len(tmp))
        return res
