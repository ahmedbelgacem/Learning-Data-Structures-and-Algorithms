class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) > 2:
            firstMax = max(nums[0], nums[1], nums[2])
            secondMax = min(max(nums[0], nums[1]),
                            max(nums[0], nums[2]), max(nums[1], nums[2]))
            thirdMax = min(nums[0], nums[1], nums[2])
            for i in range(3, len(nums)):
                if nums[i] > thirdMax:
                    thirdMax = nums[i]
                if thirdMax > secondMax:
                    secondMax, thirdMax = thirdMax, secondMax
                if secondMax > firstMax:
                    firstMax, secondMax = secondMax, firstMax
            return thirdMax
        else:
            return max(nums)
