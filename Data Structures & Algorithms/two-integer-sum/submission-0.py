class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map1 = {}

        for i in range(len(nums)):
            map1[nums[i]] = i
        
        for i in range(len(nums)):
            x = target - nums[i]

            if x in map1 and map1[x] != i:
                return [i, map1[x]]