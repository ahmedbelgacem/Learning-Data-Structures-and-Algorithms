class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        last = [1]
        result.append(last)
        for i in range(1, numRows):
            new = []
            for j in range(i + 1):
                if j == 0:
                    new.append(last[0])
                elif j == len(last):
                    new.append(last[len(last) - 1])
                else:
                    new.append(last[j - 1] + last[j])
            result.append(new)
            last = new
        return result
