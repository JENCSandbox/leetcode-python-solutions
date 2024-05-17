class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_price = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_price = max(profit, max_price)
            else:
                l = r
            r += 1

        return max_price