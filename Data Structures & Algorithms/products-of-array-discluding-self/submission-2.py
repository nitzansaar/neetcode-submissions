class Solution:

    '''
Input: nums = [1,2,4,6]
prefix = [1, 2, 8, 48]
postfix = [48,48,24,6]


    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_products = [0] * n
        prefix_products[0] = nums[0]
        for i in range(1, n, 1):
            prefix_products[i] = prefix_products[i - 1] * nums[i]
        
        postfix_products = [0] * n
        postfix_products[n - 1] = nums[n - 1]
        for i in range(n - 2, 0, -1):
            postfix_products[i] = nums[i] * postfix_products[i + 1]
        
        result = [0] * n
        for i in range(n):
            if i == 0:
                result[i] = postfix_products[i + 1]
            elif i == n - 1:
                result[i] = prefix_products[n - 2]
            else:
                result[i] = prefix_products[i - 1] * postfix_products[i + 1]
        return result

        
