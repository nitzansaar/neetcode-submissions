class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float("inf")
        high = float("-inf")
        low_index = -1
        for i in range(len(prices)):
            if prices[i] > high and i > low_index:
                high = prices[i]
            if prices[i] < low:
                low = prices[i]
                low_index = i
                # if we reach a new low price, reset high
                high = low
            profit = max(profit, (high - low))
        return profit


