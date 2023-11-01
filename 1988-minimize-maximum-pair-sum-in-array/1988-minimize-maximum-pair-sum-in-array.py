class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        i = 0
        n = len(nums)
        while(i < n//2 + 1):
            res = max(res, nums[i] + nums[n - i -1])
            i +=1
        return res