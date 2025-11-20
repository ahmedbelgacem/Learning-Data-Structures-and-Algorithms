class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        nums = []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        for interval in reversed(sorted_intervals):
            n = 0
            for num in nums:
                if num in range(interval[0], interval[1] + 1):
                    n+=1
                if n == 2:
                    break
            i = interval[0]
            while n < 2:
                while(i in nums):
                    i += 1
                nums.append(i)
                n+=1
        return len(nums)