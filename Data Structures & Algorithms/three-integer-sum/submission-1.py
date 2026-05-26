class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we want to return the triplets of values
        # that add up to 0 without duplicates

        # we should sort the array so that we can iterate over it
        # while easily skipping duplicates

        nums.sort()
        res = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue # bc we want to skip duplicates
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: # dont want dup
                        l += 1
                elif threeSum < 0: # want to increase threeSum
                    l += 1
                else: # want to decrease threeSum
                    r -= 1
        return res

            