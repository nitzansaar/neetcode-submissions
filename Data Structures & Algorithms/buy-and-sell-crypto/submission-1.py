class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0

        for price in prices:
            min_price = min(price, min_price)
            best = max(best, (price - min_price))
        
        return best

