class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)
        special = s[0]
        i = 1
        while i < len(s):
            if s[i] == s[i - 1]:
                special += s[i]
            else:
                d[special] += 1
                if len(special) > 1:
                    d[special[:-1]] += 2
                    if len(special) > 2:
                        d[special[:-2]] += 3
                special = s[i]
            i += 1
        d[special] += 1
        if len(special) > 1:
            d[special[:-1]] += 2
            if len(special) > 2:
                d[special[:-2]] += 3
        maximum = -1
        for key in d:
            if d[key] >= 3:
                maximum = max(maximum, len(key))
        return maximum