class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word) - numFriends + 1
        max_char = max(word)
        indices = [i for i, c in enumerate(word) if c == max_char]
        res = []
        for idx in indices:
            i = idx
            s = ""
            while idx < len(word) and idx < i + n:
                s+=word[idx]
                idx += 1
            res.append(s)
        return max(res)
