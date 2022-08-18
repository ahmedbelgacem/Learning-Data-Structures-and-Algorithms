class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return not(bool(moves.count('U')-moves.count('D')) or bool(moves.count('L')-moves.count('R')))