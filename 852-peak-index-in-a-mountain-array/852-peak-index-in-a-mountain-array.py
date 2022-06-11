class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)-1):
            if arr[i] > max(arr[i+1:]) and arr[i] > max(arr[:i]):
                return i
