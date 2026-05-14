class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left is buy , right is sell
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            #Check if it is profitable
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit,profit)
            else:
                left = right
            right += 1
        return max_profit
                
        