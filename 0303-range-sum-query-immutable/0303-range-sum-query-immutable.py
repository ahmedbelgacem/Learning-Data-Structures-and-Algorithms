class NumArray:

    def __init__(self, nums: List[int]):
        self.numarray = nums
        for i in range(1, len(self.numarray)):
            self.numarray[i] = self.numarray[i] + self.numarray[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.numarray[right]
        else:
            return self.numarray[right] - self.numarray[left - 1]
