class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        maximum = 0
        for idx, jump in enumerate(nums):
            if idx <= maximum:
                maximum = max(maximum, idx + jump)
                print(maximum)
        if len(nums) - 1 <= maximum:
            return True
        return False