from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        tmp = []
        for el in nums:
            if not d[el]:
                tmp.append(el)
            d[el]+=1
        tmp.sort(reverse = True, key = lambda x: d[x])
        return tmp[:k]
