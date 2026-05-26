class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in numHash:
                return [numHash[dif], i]
            numHash[nums[i]] = i
