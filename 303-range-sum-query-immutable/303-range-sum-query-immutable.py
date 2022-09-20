class NumArray:

    def __init__(self, nums: List[int]):
        self.numarray = nums
        for i in range(1,len(self.numarray)):
            self.numarray[i] = self.numarray[i] + self.numarray[i - 1]
        print(self.numarray)
    def sumRange(self, left: int, right: int) -> int:
        if not left: return self.numarray[right]
        else:
            return self.numarray[right] - self.numarray[left - 1]  

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)