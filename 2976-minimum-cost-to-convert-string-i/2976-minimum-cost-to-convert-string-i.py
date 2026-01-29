class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10000000
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for i in range(len(cost)):
            init_cost = dist[ord(original[i]) - 97][ord(changed[i]) - 97]
            dist[ord(original[i]) - 97][ord(changed[i]) - 97] = min(cost[i], init_cost)
        for intermediate in range(26):
            for start in range(26):
                for end in range(26):
                    dist[start][end] = min(dist[start][end], dist[start][intermediate] + dist[intermediate][end])
        result = 0
        for i in range(len(source)):
            s, t = ord(source[i]) - 97, ord(target[i]) - 97
            if dist[s][t] == INF:
                return -1
            else:
                result += dist[s][t]
        return result