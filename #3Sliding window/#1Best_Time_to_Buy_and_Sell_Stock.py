class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice =  prices[0]
        profit = 0

        for i in prices[1:]:
            minPrice = min(minPrice,i)
            profit = max(profit,i-minPrice)

        return profit
        