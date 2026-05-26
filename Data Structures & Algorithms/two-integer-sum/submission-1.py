class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in num_map:
                return [num_map[dif], i]
            num_map[nums[i]] = i
        return 
            