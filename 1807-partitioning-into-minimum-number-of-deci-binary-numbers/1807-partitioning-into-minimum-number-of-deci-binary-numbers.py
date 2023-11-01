class Solution:
    def minPartitions(self, n: str) -> int:
        maxi=0
        for i in range(len(n)):
            if int(n[i]) > maxi:
                maxi = int(n[i])
        return maxi
