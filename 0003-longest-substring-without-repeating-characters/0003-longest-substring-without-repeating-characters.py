class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        maxi = 0
        tmp = ""
        for idx, c in enumerate(s):
            tmp = c
            for d in s[idx+1:]:
                if d not in tmp:
                    tmp += d
                else:
                    maxi=max(maxi, len(tmp))
                    break 
                maxi = max(maxi,len(tmp))
        return max(maxi,len(tmp))