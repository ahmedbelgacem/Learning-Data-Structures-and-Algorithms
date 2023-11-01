class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i = -1
        res = 0
        c = capacity
        while i!= len(plants)-1:
            if(plants[i+1]<=c):
                i += 1
                c -= plants[i]
                plants[i] = 0
                res += 1
            else:
                res += i+1
                i = -1
                c = capacity
        return res