class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxi = arr[0]
        e = 0
        for i in range(1, len(arr)):
            if arr[i] > maxi:
                maxi = arr[i]
                e = 1
            else:
                e += 1
            if e == k:
                return maxi
        return maxi