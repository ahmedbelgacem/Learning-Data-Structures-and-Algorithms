class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        for w in text.split():
            check = True
            for l in brokenLetters:
                if l in w:
                    check = False
            if check:
                res += 1
        return res