class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize the hashmap for storing index and number
        count = {}
        #iterate through the list
        for i in range(len(nums)):
            j = target - nums[i]
            #check if the value and index are already in the map
            if j in count:
                return [count[j],i]
            count[nums[i]] = i
        return []
                

        
        