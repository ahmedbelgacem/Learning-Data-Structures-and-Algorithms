class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        for i in range(len(nums)):
            if nums[i] == key:
                b_inf = max(0, i - k)
                b_sup = min(len(nums) - 1, i + k)
                res.update(range(b_inf, b_sup + 1))
        return list(res)
