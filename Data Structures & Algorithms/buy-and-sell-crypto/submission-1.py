class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #you wanna buy it at a lower value and sell it at a higher one 
        #keep track of low as long as its before high and then 
        if not prices or len(prices) == 1: 
            return 0 
        
        max_profit = 0
        lowest_coin = prices[0]
        highest_coin = 0
        for i in range(1, len(prices)): 
            curr_profit = 0 
            if prices[i] > lowest_coin: 
                curr_profit = prices[i] - lowest_coin
                if curr_profit > max_profit:
                    max_profit = curr_profit 
            else: 
                lowest_coin = prices[i]

        return max_profit


