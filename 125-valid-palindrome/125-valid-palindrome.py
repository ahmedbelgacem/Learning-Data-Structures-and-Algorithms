class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = list("".join(filter(str.isalnum, s.lower())))
        backward = forward.copy()
        backward.reverse()
        return backward == forward
