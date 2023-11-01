class Solution:
    def isPalindrome(self, s: str) -> bool:
        begining = 0
        end = len(s) - 1
        while begining <= end:
            while(not s[begining].isalnum() and begining < end) : begining += 1
            while(not s[end].isalnum() and begining < end) : end -= 1
            if s[begining].lower() != s[end].lower():
                return False
            begining += 1
            end -=1
        return True