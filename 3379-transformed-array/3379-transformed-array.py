class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            if not nums[i]:
                result.append(0)
            elif nums[i] > 0:
                result.append(nums[(i+nums[i])%n])
            else:
                result.append(nums[(i-abs(nums[i]))%n])
        return result