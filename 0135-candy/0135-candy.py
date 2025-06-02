from collections import defaultdict
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        d = defaultdict(list)
        candies = [0] * n
        if n == 1:
            return 1
        if ratings[0] <= ratings[1]:
            candies[0] = 1
        else:
            d[ratings[0]].append(0)
        if ratings[n - 1] <= ratings[n - 2]:
            candies[n - 1] = 1
        else:
            d[ratings[n-1]].append(n-1)
        for i in range(1, n - 1):
            if ratings[i] <= ratings[i + 1] and ratings[i] <= ratings[i - 1]:
                candies[i] = 1
            else:
                d[ratings[i]].append(i)
        remaining = list(d.keys())
        remaining.sort()
        for rating in remaining:
            for position in d[rating]:
                if position == 0:
                    candies[0] = candies[1] + 1
                elif position == n - 1:
                    candies[n - 1] = candies[n - 2] + 1
                else:
                    candies[position] = 1
                    if ratings[position] > ratings[position - 1]:
                        candies[position] = candies[position - 1] + 1
                    if ratings[position] > ratings[position + 1]:
                        candies[position] = max(candies[position], candies[position + 1] + 1)
        print(candies)
        return(sum(candies))