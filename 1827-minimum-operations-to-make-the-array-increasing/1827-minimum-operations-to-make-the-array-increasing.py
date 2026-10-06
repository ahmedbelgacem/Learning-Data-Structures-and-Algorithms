class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = 0
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= last:
                s += last - nums[i] + 1
                last = last + 1
            else:
                last = nums[i]
        return s