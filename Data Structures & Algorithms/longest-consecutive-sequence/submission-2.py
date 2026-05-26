class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       res = 0
       num_set = set()
       for num in nums:
        num_set.add(num) 
       for num in num_set:
        sequence_length = 1
        cur_num = num
        while (cur_num+1 in num_set):
            sequence_length+=1
            cur_num+=1
        res = max(res, sequence_length)
       return res

