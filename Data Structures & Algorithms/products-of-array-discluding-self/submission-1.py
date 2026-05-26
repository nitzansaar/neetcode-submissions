class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            # if i == 0 or i == len(nums) - 1
            # then we get the product of all the elems
            # to the right or left respectively
            l, r = 0, len(nums) - 1
            while l < i or r > i:
                if l < i:
                    product *= nums[l]
                    l += 1
                if r > i:
                    product *= nums[r]
                    r -= 1
            # in every other case, we would need to define a 
            # left and right pointer to get the product
            # of array except self
            res.append(product)
        return res
            