class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic[target-num] = i
        print(dic)
        for i in range(len(nums)):
            if nums[i] in dic.keys() and dic[nums[i]] != i:
                return [i, dic[nums[i]]]
