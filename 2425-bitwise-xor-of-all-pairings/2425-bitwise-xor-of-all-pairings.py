class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums2) % 2 == 1:
            for el in nums1:
                res = res ^ el
        if len(nums1) % 2 == 1:
            for el in nums2:
                res = res ^ el
        return res
