class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = []
        res.append(nums[0])
        for i in range(1,len(nums)):
            res.append(max(nums[i],nums[i] + res[i - 1]))
        return(max(res))   
            
