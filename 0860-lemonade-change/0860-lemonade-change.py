class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        nb5 = 0
        nb10 = 0
        for bill in bills:
            if bill == 5:
                nb5 += 1
            if bill == 10:
                nb5 -= 1
                nb10 += 1
            if bill == 20:
                nb5 -= 1
                nb10 -= 1
            if nb5 < 0 or nb10 + nb5 / 2 < 0:
                return False
        return True
