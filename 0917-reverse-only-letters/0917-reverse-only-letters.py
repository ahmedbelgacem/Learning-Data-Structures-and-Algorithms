class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        b = []
        string = ""
        for idx, c in enumerate(s):
            if (ord(c)>= 65 and ord(c) <= 90) or (ord(c)>= 97 and ord(c) <= 122):
                string = c+string
            else:
                b.append((idx, c))
        string = list(string)
        for el in b:
            string.insert(el[0], el[1])
        string = ''.join(string)
        return string