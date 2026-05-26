class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create an empty array size len(nums)
        # where each index corresponds to the counts
        # of that variable

        # each index can hold more than one variable
        # so be prepared to have an array in the index

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            #start from the last bucket and go inwards
            for item in buckets[i]:
                res.append(item)
                if len(res) == k:
                    return res
        return res

