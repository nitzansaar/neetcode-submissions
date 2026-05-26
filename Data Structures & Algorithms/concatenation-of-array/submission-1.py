class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n*2):
            if i < n: # we are in range so make it equal
                ans.append(nums[i])
            else:# we are out of range, so go back to the front of nums
                ans.append(nums[i - n])
        return ans