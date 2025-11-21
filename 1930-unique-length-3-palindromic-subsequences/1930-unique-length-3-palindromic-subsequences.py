from collections import defaultdict
class Solution:
    def count(self, s:str, start: int, end: int):
        tmp = set()
        for letter in s[start + 1 : end]:
            tmp.add(letter)
        return len(list(tmp))

    def countPalindromicSubsequence(self, s: str) -> int:
        d = defaultdict(int)
        d2 = defaultdict(list)
        res = 0
        for idx, letter in enumerate(s):
            d[letter]+=1
            d2[letter].append(idx)
        for key, value in d.items():
            if value >= 2:
                end = d2[key][len(d2[key]) - 1]
                start = d2[key][0]
                res+= self.count(s, start, end)
        return res
                