class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use a set
        #keep track of current longest sequence
        # use sliding window 

        #return the max length
    
        seen = set()
        res = 0

        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            # no more duplicates
            res = max(res, (r - l + 1))
            seen.add(s[r])
        return res