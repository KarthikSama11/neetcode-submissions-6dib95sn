class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftmin = prices[0]
        res = 0
        for price in prices:
            profit = price - leftmin
            res = max(profit, res)
            leftmin = min(price, leftmin)
        return res