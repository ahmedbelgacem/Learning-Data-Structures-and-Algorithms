class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)
        for idx, char in enumerate(s):
            d[char] += 1
            i = 1
            while idx+i < len(s):
                if s[idx+i] == s[idx]: 
                    d[s[idx: idx+i+1]] +=1
                    i+=1
                else:
                    break
        maximum = -1
        for key in d:
            if d[key] >= 3:
                maximum = max(maximum, len(key))
        return maximum