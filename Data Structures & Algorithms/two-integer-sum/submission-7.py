class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            dif = target - nums[i]
            if dif in numMap:
                return [numMap[dif],i]
            numMap[nums[i]] = i
        