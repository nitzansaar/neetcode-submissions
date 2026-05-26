class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float("-inf")
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                curr_height = min(heights[i], heights[j])
                curr_width = j - i
                area = curr_height * curr_width
                res = max(res, area)
        return res
