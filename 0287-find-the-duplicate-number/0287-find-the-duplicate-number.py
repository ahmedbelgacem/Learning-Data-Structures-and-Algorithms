from collections import defaultdict
def def_value():
    return 0
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(def_value)
        for el in nums:
            d[el]+=1
            if d[el] == 2:
                return el