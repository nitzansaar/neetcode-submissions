class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        for num in nums:
            if num_count.get(num):
                return True
            num_count[num] = True
        return False

            
        

         