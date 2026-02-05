import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort(reverse=True)
        i = 0
        n = len(gifts)
        while i < k:
            el = gifts.pop(0)
            el = floor(math.sqrt(el))
            j = next(
                (
                    i
                    for i, value in enumerate(gifts)
                    if value < el
                ),
                n,
            )
            gifts.insert(j, el)
            i +=1
        return sum(gifts)