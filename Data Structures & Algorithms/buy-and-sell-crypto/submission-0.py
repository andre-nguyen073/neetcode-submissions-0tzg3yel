class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 
        if the array is strictly descending you wont make any profit
        if the array is ascending you can make money
        """
        res = 0
        #only can buy and can not sell
        if len(prices) == 1: 
            return res

        l = 0 
        for r in range(1, len(prices)): 
            #you can turn a profit
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l] 
                if profit > res: 
                    res = profit 
            elif prices[l] >= prices[r]: 
                l = r

        return res