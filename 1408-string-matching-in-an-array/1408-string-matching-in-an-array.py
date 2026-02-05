class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        seen = []
        res = set()
        for i, w in enumerate(words):
            for s in seen:
                if w in s:
                    res.add(w)
            for s in words[i + 1 : ]:
                if w in s:
                    res.add(w)
            seen.append(w)
        return list(res)