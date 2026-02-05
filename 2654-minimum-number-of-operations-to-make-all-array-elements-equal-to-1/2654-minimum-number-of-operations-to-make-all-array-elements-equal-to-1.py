from math import gcd
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        one_count = 0
        g = 0
        for el in nums:
            if el == 1:
                one_count +=1
                g = gcd(g, el)
        if one_count:
            return n - one_count
        if g > 1:
            return -1
        n_sub = 2
        while n_sub <= n:
            for idx in range(n - n_sub + 1):
                val = nums[idx]
                for i in range(1, n_sub):
                    val = gcd(val, nums[idx + i])
                    if val == 1:
                        return n_sub - 1 + len(nums) - 1
            n_sub+=1
        return -1