class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)

        if len_prices < 2:
            return 0

        anchor = 0 
        total_profit = 0

        for i in range(1, len_prices):
            if not prices[i] <= prices[anchor]:
                # temp_profit = prices[i] - prices[anchor]
                # if temp_profit > total_profit:
                #     total_profit = temp_profit
                total_profit = max(total_profit, prices[i]-prices[anchor])
            else:
                anchor = i
            
        return total_profit