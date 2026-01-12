class Solution:
    def check(self, l: List[str]):
        tmp = []
        for el in l:
            if el in tmp:
                return False
            if el != ".":
                tmp.append(el)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        for ridx, row in enumerate(board):
            if not self.check(row):
                return False
            for cidx, el in enumerate(row):
                columns[cidx].append(el)
                boxes[ridx//3 *3+ cidx//3].append(el)
        for column in columns:
            if not self.check(column):
                return False
        for box in boxes:
            if not self.check(box):
                return False
        return True