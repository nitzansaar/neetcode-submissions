class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # fill hashmap with the counts
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        res = []
        for _ in range(k): # iterate through the counts hashmap k times
            max_num = -1
            max_count = 0
            for num, count in counts.items(): # go through all elems in hashmap
                if count > max_count:
                    max_count = count
                    max_num = num
            # add the curr max count to res
            res.append(max_num)
            del counts[max_num]
        return res
