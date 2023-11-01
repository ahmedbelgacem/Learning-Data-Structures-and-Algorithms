class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1
            if count > max_count:
                    max_count = count
        return max_count
