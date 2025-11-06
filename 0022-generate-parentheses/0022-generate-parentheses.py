class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            tmp = self.generateParenthesis(n-1)
            res = []
            for el in tmp:
                for i in range(len(el)):
                    if el[i] == "(":
                        for j in range(i, len(el)):
                            if el[j] == ")":
                                res.append(el[:i]+"("+el[i:j]+")"+el[j:])
                res.append(el+"()")
                res.append("()"+el)
            return list(set(res))