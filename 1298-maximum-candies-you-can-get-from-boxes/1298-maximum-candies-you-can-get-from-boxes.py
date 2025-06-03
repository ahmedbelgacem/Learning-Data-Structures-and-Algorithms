class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        res = 0
        continue_opening = True
        while initialBoxes and continue_opening:
            boxes_left = []
            for box in initialBoxes:
                if status[box] == 1:
                    res+=candies[box]
                    boxes_left.extend(containedBoxes[box])
                    for key in keys[box]:
                        status[key] = 1
                    status[box] = 0
                else:
                    boxes_left.append(box)
            initialBoxes = boxes_left
            continue_opening = False
            for box in initialBoxes:
                if status[box]:
                    continue_opening = True
        return res
