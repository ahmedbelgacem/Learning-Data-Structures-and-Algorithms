class Solution:
    def balancedStringSplit(self, s: str) -> int:
        number_r = 0
        number_l = 0
        result = 0
        for c in s:
            if c == 'R':
                number_r+=1
            elif c == 'L':
                number_l+=1
            if number_r == number_l:
                result+=1
                number_r = 0
                number_l = 0
        return result
        