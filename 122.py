class Solution(object):

    # idea: brute force, if price[i] < price[i + 1] => buy, else sell
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # buy
            if price < min_price:
                min_price = price
            # sell
            else:
                max_profit += price - min_price
                min_price = price
        
        return max_profit
