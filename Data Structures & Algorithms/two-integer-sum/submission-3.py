class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in count:
                return [count[j],i]
            count[nums[i]] = i
        return []
        