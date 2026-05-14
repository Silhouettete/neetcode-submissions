class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countNums = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in countNums:
                return [countNums[j],i]
            countNums[nums[i]] = i
        return []

        