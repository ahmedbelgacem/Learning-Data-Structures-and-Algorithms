import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]
        else:
            tmp = self.subsets(nums[:-1])
            res = copy.deepcopy(tmp)
            for el in tmp:
                el.append(nums[-1])
                res.append(el)
            return res