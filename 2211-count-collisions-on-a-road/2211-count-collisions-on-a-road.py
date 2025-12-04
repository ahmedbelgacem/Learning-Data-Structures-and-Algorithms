class Solution:
    def countCollisions(self, directions: str) -> int:
        i = 0
        j = 0

        while i < len(directions):
            if directions[i] == "L": 
                i+=1
            else:
                break
        while j < len(directions):
            if directions[len(directions) -j - 1] == "R":
                j+=1
            else:
                break
        directions = directions[i:len(directions) -j]
        return len(directions) - directions.count("S")
        